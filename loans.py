# -*- coding: utf-8 -*-
"""
Homework 4:
    Running Simulations on loans

@author: Beckett Sanderson
"""

import numpy as np
import matplotlib.pyplot as plt

LOAN = 221808
OUTCOMES = {"defaults": {"chance": 0.02, "results": 120000 + LOAN}}
NUM_LOANS = 1000
TRIALS = 10000

def one_loan(dic):
    """
    Simulates one loan to see if it defaults or not

    Parameters
    ----------
    dic : dictionary
        dictionary contiaining probability of a default.

    Returns
    -------
    loan_defaults : int
        returns 1 if the loan defaults and 0 if it does not.

    """
    loan_defaults = 0
    
    # loops through each occurence in the dictionary
    for occ in dic:
        
        # runs a choice of the default based on the probabilites
        result = np.random.choice([occ, "none"], p = [dic[occ]["chance"], 
                                               1 - dic[occ]["chance"]])
        # checks if the loan defaults
        if result == occ:
            
            loan_defaults += 1
            
    return loan_defaults


def run_experiment(dic, experiments):
    """
    Runs a set of simulations up to the number of experiments

    Parameters
    ----------
    dic : dictionary
        dictionary contiaining probability of a default.
    experiments : int
        number of experiments to run.

    Returns
    -------
    total_defaults : int
        the number of loans that defaulted.

    """
    total_defaults = 0
    
    # loops throught the number of experiments to run
    for i in range(experiments):
        
        # adds to the total number of loans that defaulted
        total_defaults += one_loan(dic)
    
    return total_defaults


def calc_interest(profit):
    """
    Calculates the interest needed to make the input profit for the year

    Parameters
    ----------
    profit : int
        the amount of profit to make after the year is over.

    Returns
    -------
    int_rate : float
        the interest rate needed to make the input profit.

    """
    # gets the number of loans that defaulted
    num_defaults = run_experiment(OUTCOMES, NUM_LOANS)
    
    # gets the total profit needed to make the profit
    total_prof_needed = profit + (num_defaults * 
                                  OUTCOMES["defaults"]["results"]) 
    
    # calculates the interest rate needed to make the profit
    int_rate = total_prof_needed / (LOAN * (1000 - num_defaults))
    
    return round(int_rate, 3)


def run_trials(trials, profit):
    """
    Runs a set of trials of loan simulations

    Parameters
    ----------
    trials : int
        number of trials to run.
    profit : int
        the amount of profit to make after the year is over.
        
    Returns
    -------
    trial_results : list
        list of the results of the trials.

    """
    trial_results = []
    
    # loops through number of trials to run
    for i in range(trials):
        
        # appends the interest rate from each trial to the list
        trial_results.append(calc_interest(profit))
        
    return trial_results


def Main():
    
    print("Welcome to Lab 4!\n")
    
    # gets the profit to make from the user
    profit = int(input("How much profit does Mr. Scrooge need???\n"))
    
    # runs a set of trials and determines the mean int rate from all trials
    loan_trials = run_trials(TRIALS, profit)
    print("The average interest rate needed is:", 
          round(np.mean(loan_trials), 4))
    
    # plots a histogram of the interest rates
    plt.hist(loan_trials, bins = 10)
    
    # graph organization
    plt.title("Interest Rate Needed for Profit")
    plt.xlabel("Average Interest Rate")
    plt.ylabel("Number of Trials")
    

if __name__ == "__main__":
    
    Main()
    