#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:58:58 2020

@author: meeps360
"""

from BankAccount import *

class CheckingAccount(BankAccount):
     
    def __init__(self, name, checking_account_id, checking_balance, per_check_fee):
        BankAccount.__init__(self, name, checking_account_id, checking_balance)
        self.per_check_fee = per_check_fee
        
    def calculateCheckFee(self, number_of_checks,):
        return self.per_check_fee * number_of_checks
    
    def __str__(self):
        return BankAccount.__str__(self)
    
    def getPerCheckingFee(self):
        return self.per_check_fee
    
    def setPerCheckingFee(self, per_fee):
        self.per_check_fee = per_fee
        
    def getBalance(self):
        return self.checking_balance