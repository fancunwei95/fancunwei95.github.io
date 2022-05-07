import numpy as np
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


class RealizedGARCH(object):
    
    def __init__(self, returns, RVs, scale = 1):
        
        self.params = {
            "omega" : 0.1,
            "beta"  : 0.1,
            "gamma" : 0.1,
            "mu"    : 0.1
        }
        self.params = pd.Series(self.params)
        self.returns_original = returns
        self.RVs_original = RVs
        self.scale = scale
        self.returns = self.returns_original*self.scale
        self.RVs = self.RVs_original*self.scale**2
        
        self.T = self.returns.shape[0]
        
    def _initialize(self, **kargs):
        for key, value in kargs.items():
            self.params[key] = value
        var = np.var(self.returns)
        self.params["mu"] = self.returns.mean()
        self.params["omega"] = var*(1-self.params[1]- self.params[2])
        self.sigma2_0 = var
        self.sigma2_0_original = var/self.scale**2
        
        
    def _get_sigmas(self, params):
        
        sigma2 = np.zeros(self.T)
        sigma2[0] = params[0] + params[1]*self.sigma2_0
        for i in range(1, len(sigma2)):
            sigma2[i] = params[0] + params[1]*sigma2[i-1] + params[2]*self.RVs[i-1]
        sigma2 = np.maximum(sigma2, 1.0e-10)
        return sigma2
    
    def get_sigmas_original(self, params):
        sigma2 = np.zeros(self.T)
        sigma2[0] = params[0] + params[1]*self.sigma2_0_original
        for i in range(1, len(sigma2)):
            sigma2[i] = params[0] + params[1]*sigma2[i-1] \
                        + params[2]*self.RVs_original[i-1]
        #sigma2 = np.maximum(sigma2, 1.0e-10)
        
        return sigma2
    
    def _get_mu(self, sigma2):
        weight = 1.0/sigma2
        mu = np.sum(self.returns*weight)/np.sum(weight)
        return mu
        
        
    def _derivative(self, params):
        sigma2 = self._get_sigmas(params)
        mu = params[-1]
        diff = self.returns - mu
        first_part = 1.0/sigma2 - (diff/sigma2)**2
        
        sigma_beta = np.zeros(self.T)
        sigma_beta[0] = self.sigma2_0 
        
        sigma_omega = np.zeros(self.T)
        sigma_omega[0] = 1 
        
        sigma_gamma = np.zeros(self.T)
        sigma_gamma[0] = 0
        
        for i in range(1, len(sigma2)):
            sigma_beta[i]  = sigma2[i-1]  +  params[1] * sigma_beta[i-1]
            sigma_omega[i] = 1 + params[1]*sigma_omega[i-1]
            sigma_gamma[i] = self.RVs[i-1] + params[1] * sigma_gamma[i-1]
        d_omega = -0.5*np.sum(first_part*sigma_omega)
        d_beta  = -0.5*np.sum(first_part*sigma_beta)
        d_gamma = -0.5*np.sum(first_part*sigma_gamma)
        d_mu    =  np.sum(diff/sigma2)
        
        return np.array([d_omega, d_beta, d_gamma, d_mu])
    
    
    def _log_likelihood(self, params):
        sigma2 = self._get_sigmas(params)
        mu = params[-1]
        diff = self.returns - mu
        loglikelihood = np.sum(diff**2/sigma2 + np.log(sigma2))
        return -0.5*loglikelihood
    
    
    def _minimize(self, tol , verbose, options):
        
        self._callback_memory = {
            "log(L)": 0.0, "iter": 0 , "mu" : self.params["mu"]
        }
        
        def negative_log_likelihood(params): 
            loglikelihood = self._log_likelihood(params)
            self._callback_memory["log(L)"] = loglikelihood
            return - loglikelihood
            
        def jacob(params):
            # negative derivative for -loglklhd, 
            return -self._derivative(params) 
        
        def callback(params, *args):
            sigma2 = self._get_sigmas(params)
            self._callback_memory["mu"] = self._get_mu(sigma2)
            it = self._callback_memory["iter"] 
            loglikelihood = self._callback_memory["log(L)"]
            self._callback_memory["iter"] +=1
            if verbose > 0 :
                if it% verbose == 0:
                    print ("\t \t iter: %d \t log(L): %4.3f" %(it, loglikelihood))
            return 
        
        bounds = [(0,None), (0,1), (0,1), (None, None)]
        constraints = [
             {"type":'ineq',
              'fun' : lambda params: 1 - params[1] - params[2] ,
              'jac' : lambda params: np.array([0,-1,-1,0])
             }]
        
        opt = minimize(
                negative_log_likelihood,
                self.params,
                method = "SLSQP",
                jac = jacob,
                bounds = bounds,
                constraints = constraints,
                tol = tol,
                callback = callback,
                options = options
               )
        return opt
        
    def _fit_measurement(self):
        y  = np.log(self.RVs_original)
        x1 = np.log(self.sigma2)
        z  = self.standard_error
        x2 = z 
        x3 = z**2-1
        
        X = np.stack([x1,x2,x3], axis = 0).T
        LR = LinearRegression()
        LR = LR.fit(X,y)
        
        self.measure_params = np.zeros(len(LR.coef_)+2)
        self.measure_params[1:-1] = LR.coef_
        self.measure_params[0] = LR.intercept_
        self.measure_params = pd.Series(self.measure_params)
        self.measure_params.index = ["xi", "phi", "tau1", "tau2", "sigmaU"]
        err = y - LR.predict(X)
        self.measure_params[-1] = np.sqrt(np.mean(err**2))
        return
        
    def measure_RV(self, sigma2 = None, standard_err = None):
        
        if sigma2 is None:
            sigma2 = self.sigma2
        if standard_err is None:
            standard_err = self.standard_error
            
        pred = self.measure_params["xi"] + self.measure_params["phi"]*np.log(sigma2)
        pred += self.measure_params["tau1"] * self.standard_error
        pred += self.measure_params["tau2"]*(self.standard_error**2-1)
        
        pred = np.exp(pred)
        
        return pred
    
    def _fit_volatility(self, tol, verbose, options):
        betas = np.linspace(0.1, 0.9, 5)
        gammas = np.linspace(0.1, 0.9, 5)
        best_L = None
        best_opt = None
        for b in betas:
            for g in gammas:
                if b + g >= 0.99 :
                    continue
                if verbose > 0:
                    print ("\t Trial: beta0: %.2f\t gamma0: %.2f: "%(b,g))
                self._initialize(beta = b, gamma = g)
                L0 = self._log_likelihood(self.params)
                opt = self._minimize(tol, verbose, options)
                if opt.status != 0:
                    
                    print ("\t Optimizer Issue: ", opt.message)
                        
                it = self._callback_memory["iter"]
                L1 = self._log_likelihood(opt.x)
                deltaL = L1 - L0
                if verbose > 0:
                    print ("\t iter: %d \t log(L0): %4.3f \t log(L1): %4.3f \t delta L : %.3f" %(it, L0, L1, deltaL))
                if best_L is None:
                    best_L = L1
                    best_opt = opt
                    continue
                if L1 > best_L:
                    best_L = L1
                    best_opt = opt
        print ("\t best L1 = %4.3f" % best_L)
        return best_opt
    
    def _set_params_from_opt(self, opt):
        self.params[:] = opt.x
        self.params["mu"] /= self.scale
        self.params["omega"] /= self.scale**2
        self.sigma2_0 = self.sigma2_0_original
        return
    
    def fit(self, tol = None, verbose = 10, options = {}):
        
        opt = self._fit_volatility(tol, verbose, options)
        self._set_params_from_opt(opt)
        
        self.sigma2 = self.get_sigmas_original(self.params)  
        self.sigma2 = pd.Series(self.sigma2)
        self.sigma2.index = self.returns.index
        
        
        self.standard_error = (self.returns_original-self.params["mu"])
        self.standard_error /= np.sqrt(self.sigma2)
        
        self._fit_measurement()
        return
            
    def plot(self, ax = None,**kwargs):
        if ax is None:
            f, ax = plt.subplots(figsize = fig_size)
        ax.plot(self.RVs_original, label = "RVs")
        ax.plot(self.sigma2, label = "sigma2")
        #ax.plot(self.returns**2, label = "r2")
        ax.legend(loc = "best")
        return 
    
    def train_log_likelihood(self):
        return -0.5*np.sum(np.log(2.0*np.pi*(self.sigma2) ) + self.std()**2)
    
    def std(self):
        return self.standard_error
    
    def predict_single(self, horizon, standard_err = None):
        
        sigma2 = np.zeros(horizon+1)
        last_RV = self.RVs_original[-1]
        pred_RVs = np.zeros(horizon+1)
        sigma2[0] = self.sigma2[-1]
        xi, phi, tau1, tau2, sigmaU = list(self.measure_params[:]) 
        last_z = self.standard_error[-1]
        if standard_err is None:
            errors = np.random.normal(shape=(horizon,))
        else:
            errors = standard_err
    
        for i in range(1, horizon+1):
            sigma2[i] = self.params["omega"] + self.params["beta"]*sigma2[i-1] +\
                        self.params["gamma"]*last_RV
            last_RV = xi + phi * np.log(sigma2[i]) + tau1*last_z \
                            + tau2*(last_z**2-1) + np.random.normal()*sigmaU
            last_RV = np.exp(last_RV)
            pred_RVs[i] = last_RV
            last_z = errors[i-1]
        return sigma2[1:], pred_RVs[1:]
    
    def predict(self, horizon, n_sample=1000, 
                quantiles = np.array([0.05, 0.5, 0.95]), 
                standard_err = None ):
        sigma2_pred = np.zeros((n_sample, horizon))
        RV_pred = np.zeros((n_sample, horizon))
        for i in range(n_sample):
            sigma2, RV = self.predict_single(horizon, standard_err[i,:])
            sigma2_pred[i,:] = sigma2
            RV_pred[i,:] = RV
            
        sigma2 = np.quantile(sigma2_pred, quantiles, axis = 0)
        RV = np.quantile(RV_pred, quantiles, axis = 0)
        return sigma2, RV
    
    




class DCCModel(object):
    def __init__(self, noises):
        
        self.noises = noises
        self.params ={
            "a" : 0.1, "b" : 0.1
        }
        self.params = pd.Series(self.params)
        self.T = self.noises.shape[0]
        self.m = self.noises.shape[1]
        self.noises_arr = self.noises.to_numpy()
        self._initialize()
        
        
    def _initialize(self, **args):
        for k,val in args.items():
            self.params[k] = val
        
        self.S = self.noises.T.dot(self.noises)/self.noises.shape[0]
        self.S = self.S.to_numpy()
        
    def _getC(self, params, return_lastQ = False):
        
        C_t = np.zeros((self.T, self.m,self.m))
        lastQ = 5.0*self.S
        S = self.S
        corrS = S/np.sqrt(np.diag(S))/np.sqrt(np.diag(S)[:,None])
        for i in range(self.T):
            z = self.noises_arr[i,:]
            a,b = params[0], params[1]
            Q = S*(1-a -b) + a * z[:,None] * z[None,:] + b*lastQ
            diag = np.maximum(np.diag(Q), 1.0e-10)
            np.fill_diagonal(Q, diag) 
            C = (Q/np.sqrt(diag))/np.sqrt(diag[:,None])
            while np.linalg.det(C) <= 1.0e-10:
                Q = S + np.random.uniform()*(b)*np.identity(Q.shape[0])\
                    +np.random.uniform()*a*z[:,None] * z[None,:]
                diag = np.maximum(np.diag(Q), 1.0e-10)
                C = (Q/np.sqrt(diag))/np.sqrt(diag[:,None])
            C_t[i,:,:] = C
            lastQ = np.copy(Q)
        if return_lastQ:
            return C_t, lastQ
        return C_t
    
    def _log_likelihood(self, C_t):
        
        z = self.noises_arr
        dets = np.linalg.det(C_t)
        y = np.linalg.solve(C_t, z)
        zCz = np.sum(z*y, axis = -1)
        zz = np.sum(z*z, axis = -1)
        llk = -0.5*np.sum(np.log(dets) + zCz - zz)
        return llk
    
    def _minimize(self, tol, options):
        
        call_back = {
            "iteration": 0, 
            "log(L)" : 0
        }
        
        def neg_loglikelihood(params):
            C = self._getC(params)
            return -self._log_likelihood(C)
        
        def callback(params, **args):
            
            call_back["log(L)"] =  -neg_loglikelihood(params)
            if call_back["iteration"] > 0:
                print ("iteration: %d \t log(L): %4.3f \t a: %.5g \t b:%.5g"
                      %(call_back["iteration"],call_back["log(L)"], 
                        params[0], params[1] )
                      )
            call_back["iteration"] +=1
            
        bounds = [(0,1), (0,1)]
        constraints = [
             {"type":'ineq',
              'fun' : lambda params: 1 - params[0] - params[1] ,
              'jac' : lambda params: np.array([-1,-1])
             }]
        
        opt = minimize(
                neg_loglikelihood,
                self.params,
                method = "SLSQP",
                bounds = bounds,
                constraints = constraints,
                tol = tol,
                callback = callback,
                options = options
               )
        return opt 
    
    def fit(self, a = 0.3, b = 0.1, tol = None, options = {}):
        self._initialize(a = a, b = b)
        opt = self._minimize(tol, options)
        self.params[:] = opt.x
        self.Ct, self.lastQ = self._getC(self.params, return_lastQ = True)
        self.loglikelihood = self._log_likelihood(self.Ct)
        
    
    def predict_single(self, horizon, returnz = True):
        lastQ = self.lastQ
        lastz = self.noises_arr[-1,:]
        resz = np.zeros((horizon, self.m))
        a,b = self.params["a"], self.params["b"]
        resC = np.zeros(shape=(horizon, self.m, self.m))
        for i in range(horizon):
            Q = self.S*(1.0-a-b) + a*lastz[None,:]*lastz[:,None] + b * lastQ
            diag = np.diag(Q)
            C = (Q/np.sqrt(diag))/np.sqrt(diag[:,None]) 
            resz[i,:] = np.random.multivariate_normal(np.zeros(self.m), C)
            lastz[:] = resz[i,:]
            lastQ[:,:] = Q[:,:]
            resC[i,:,:] = C
        if returnz:
            return resC, resz
        return resC


    
    

class RGARCH_DCC(object):
    def __init__(self, train, garch_scale = 1):
        self.traindata = train
        self.stocks = train.columns.get_level_values(0).unique()
        self.m = len(self.stocks)
        self._initialize(garch_scale)
        self.DCC = None
        
    def _initialize(self, garch_scale):
        GARCHs = {}
        for symbol in self.stocks:
        
            returns = self.traindata[symbol]["return"]
            RVs = self.traindata[symbol]["RV"]
            rl_garch = RealizedGARCH(returns, RVs, scale = garch_scale)
            GARCHs[symbol] = rl_garch 
        
        self.GARCHs = GARCHs
        
    def fit(self,tol = None, verbose = 10, GARCH_options = {}, DCC_options = {},
           **kwargs):
        PARAMs = {}
        for s in self.GARCHs:
            rl_garch = self.GARCHs[s]
            print ("fit %s ..." %(s))
            rl_garch.fit(verbose = verbose, tol = tol, options = GARCH_options)
            params = pd.concat( (rl_garch.params, rl_garch.measure_params) ) 
            PARAMs[s] = params
        self.GARCH_PARAMs = pd.DataFrame.from_dict(PARAMs, orient="columns")
        std = {}
        for s, garch in self.GARCHs.items():
            std[s] = garch.std()
        std = pd.DataFrame.from_dict(std, orient = "columns")
        self.STD = std
        self.DCC = DCCModel(std)
        self.DCC.fit(tol = tol, options = DCC_options,**kwargs)
        self.DCC_PARAMs = self.DCC.params
        
        
    def params(self):
        print ("rGarch parameters:")
        print (self.GARCH_PARAMs)
        
        print ()
        print ("DCC parameters:")
        print (self.DCC_PARAMs)
        
    def predict_horizon_single(self, horizon):
        resC, noises = self.DCC.predict_single(horizon)
        sigma2_pred = np.zeros((horizon, self.m))
        RV_pred = np.zeros((horizon, self.m))
        for i in range(self.m):
            symbol = self.stocks[i]
            err = noises[:, i]
            sigma2, RV = self.GARCHs[symbol].predict_single(horizon, 
                                                            standard_err = err)
            sigma2_pred[:,i] = sigma2
            RV_pred[:,i] = RV
        return sigma2_pred, RV_pred, resC
    
    def predict_horizon(self, horizon, n_sample = 1000, low_q = 0.1, high_q = 0.9):
        quantiles = np.array([low_q, 0.5, high_q])
        sigma2 = np.zeros((n_sample, horizon, self.m))
        RVs = np.zeros((n_sample, horizon, self.m))
        for i in range(n_sample):
            sigma2_pred, RV_pred, _ = self.predict_horizon_single(horizon)
            sigma2[i,:,:] = sigma2_pred
            RVs[i, :, :] = RV_pred
        sigma2 = np.quantile(sigma2, quantiles, axis=0)
        RVs = np.quantile(RVs, quantiles, axis = 0)
        return sigma2, RVs
    
    def predict_horizon_portfolio(self, horizon, weights,
                                 n_sample = 1000, low_q = 0.1, high_q = 0.9):
        quantiles = np.array([low_q, 0.5, high_q])
        sigma2 = np.zeros((n_sample, horizon))
        for i in range(n_sample):
            sigma2_pred, RV_pred, C_pred = self.predict_horizon_single(horizon)
            sigma_pred = np.sqrt(sigma2_pred)
            u = sigma_pred*weights
            portfolio_pred = np.sum(u*np.matmul(C_pred, u[...,None])[...,0], 
                                    axis = 1)
            sigma2[i,:] = portfolio_pred
        return np.quantile(sigma2, quantiles, axis = 0)
    
    def get_portfolio_sigma2(self, weights):
        Ct = self.DCC.Ct
        sigma2 = np.zeros((self.traindata.shape[0], self.m))
        for i in range(self.m):
            symbol = self.stocks[i]
            sigma2[:,i] = self.GARCHs[symbol].sigma2
        sigma = np.sqrt(sigma2)
        u = sigma*weights
        portfolio = np.sum(u*np.matmul(Ct, u[...,None])[...,0], axis=1)
        portfolio = pd.Series(portfolio)
        portfolio.index = self.traindata.index
        return portfolio
            