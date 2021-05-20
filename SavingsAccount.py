#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:07:55 2020

@author: meeps360
"""

from BankAccount import *

class SavingsAccount(BankAccount):
    
    def __init__(self, name, savings_account_id, saving_balance, per_transaction_fee):
        BankAccount.__init__(self, name, savings_account_id, saving_balance)
        self.per_transaction_fee = per_transaction_fee
        
    def calculateFee(self, number_of_transactions):
        return self.per_transaction_fee * number_of_transactions
    
    def __str__(self):
        return BankAccount.__str__(self)
    
    def getPerTransactionFee(self):
        return self.per_transaction_fee
    
    def setPerTransactionFee(self, per_fee):
        self.per_transaction_fee = per_fee
    
    def getBalance(self):
        return self.savings