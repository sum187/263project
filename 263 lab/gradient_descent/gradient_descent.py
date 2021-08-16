# ENGSCI263: Gradient Descent Calibration
# gradient_descent.py

# PURPOSE:
# IMPLEMENT gradient descent functions.

# PREPARATION:
# Notebook calibration.ipynb.

# SUBMISSION:
# Show the instructor that you can produce the final figure in the lab document.

# import modules
import numpy as np


# **this function is incomplete**
#					 ----------
def obj_dir(obj, theta0, model=None):
    """ Compute a unit vector of objective function sensitivities, dS/dtheta0.

        Parameters
        ----------
        obj: callable
            Objective function.
        theta0: array-like
            Parameter vector at which dS/dtheta0 is evaluated.
        
        Returns
        -------
        s : array-like
            Unit vector of objective function derivatives.

    """
    # empty list to store components of objective function derivative 
    s = np.zeros(len(theta0))
    
    # compute objective function at theta0
    # **uncomment and complete the command below**
    s0 = obj(theta0)

    # amount by which to increment parameter
    dtheta0 = 1.e-2
    
    # for each parameter
    for i in range(len(theta0)):
        # basis vector in parameter direction 
        eps_i = np.zeros(len(theta0))
        eps_i[i] = 1
        
        # compute objective function at incremented parameter
        # **uncomment and complete the command below**
        si = obj(theta0+eps_i*dtheta0) 

        # compute objective function sensitivity
        # **uncomment and complete the command below**
        s[i] = (si-s0)/dtheta0

    # return sensitivity vector
    return s


# **this function is incomplete**
#					 ----------
def step(theta0, s, alpha):
    """ Compute parameter update by taking step in steepest descent direction.

        Parameters
        ----------
        theta00 : array-like
            Current parameter vector.
        s : array-like
            Step direction.
        alpha : float
            Step size.
        
        Returns
        -------
        theta01 : array-like
            Updated parameter vector.
    """
    
    return -s*alpha+theta0

# this function is complete
def line_search(obj, theta0, s):
    """ Compute step length that minimizes objective function along the search direction.

        Parameters
        ----------
        obj : callable
            Objective function.
        theta0 : array-like
            Parameter vector at start of line search.
        s : array-like
            Search direction (objective function sensitivity vector).
    
        Returns
        -------
        alpha : float
            Step length.
    """
    # initial step size
    alpha = 0.
    # objective function at start of line search
    s0 = obj(theta0)
    # anonymous function: evaluate objective function along line, parameter is a
    sa = lambda a: obj(theta0-a*s)
    # compute initial Jacobian: is objective function increasing along search direction?
    j = (sa(.01)-s0)/0.01
    # iteration control
    N_max = 500
    N_it = 0
    # begin search
        # exit when (i) Jacobian very small (optimium step size found), or (ii) max iterations exceeded
    while abs(j) > 1.e-5 and N_it<N_max:
        # increment step size by Jacobian
        alpha += -j
        # compute new objective function
        si = sa(alpha)
        # compute new Jacobian
        j = (sa(alpha+0.01)-si)/0.01
        # increment
        N_it += 1
    # return step size
    return alpha

# this function is complete
def gaussian2D(theta0, model=None):
    """ Evaluate a 2D Gaussian function at theta0.

        Parameters
        ----------
        theta0 : array-like 
            [x, y] coordinate pair.
        model : callable
            This input always ignored, but required for consistency with obj_dir.
        
        Returns
        -------
        z : float
            Value of 2D Gaussian at theta0.
    """
    # unpack coordinate from theta0
    [x, y] = theta0
    # function parameters (fixed)
        # centre
    x0 = -.2 		
    y0 = .35
        # widths
    sigma_x = 1.2
    sigma_y = .8
    # evaluate function
    return  1-np.exp(-(x-x0)**2/sigma_x**2-(y-y0)**2/sigma_y**2)

    