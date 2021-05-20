#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:03:02 2020

@author: meeps360
"""

class BankAccount(object):
    
    def __init__(self, name, account_id, balance):
        self.name = name
        self.account = account_id
        self.balance = balance
        
    def __str__(self):
        return "Name: " + str(self.name) + "   Account ID: " + str(self.account) + \
            "   Balance: " + str(self.balance)
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawl(self, amount):
        if self.balance>amount:
            self.balance -= amount
        
        else:
            return "Insufficient funds"
