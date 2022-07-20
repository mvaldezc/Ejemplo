#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:02:13 2022

@author: esbeidytorres
"""

import pandas as pd
pfmodule_dataframe = pd.read_csv('gdb_pfmodule.csv')
pf_extract = pd.read_csv("gdb_extract.csv")


def compare (variable_choice, pfmodule_dataframe = pd.read_csv('gdb_pfmodule.csv')) : 
    new_dataframe = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 4) \
                            & (pfmodule_dataframe["pillar"] == "Availability") \
                            & (pfmodule_dataframe["data_type"] == "response") 
                            & (pfmodule_dataframe["variable_name"] == variable_choice)]
    return new_dataframe

def compareg (variable_choice, pfmodule_dataframe = pd.read_csv('gdb_pfmodule.csv')) : 
    new_dataframe = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 4) \
                            & (pfmodule_dataframe["pillar"] == "Governance") \
                            & (pfmodule_dataframe["data_type"] == "response") 
                            & (pfmodule_dataframe["variable_name"] == variable_choice)]
    return new_dataframe

def compares (variable_choice, pf_extract = pd.read_csv("gdb_extract.csv")) : 
    new_dataframe = pf_extract[(pf_extract["hierarchy_level"] == 4) \
                            & (pf_extract["pillar"] == "Availability") \
                            & (pf_extract["data_type"] == "response") 
                            & (pf_extract["variable_name"] == variable_choice)]
    return new_dataframe

#####ANALISIS ESPECIAL

df_e_proposed = compares("A.PF.BUDGETSPEND.e.e1.PROPOSED",)
e_proposed = df_e_proposed["response"].value_counts()

df_e_approved = compares("A.PF.BUDGETSPEND.e.e1.APPROVED",)
e_approved = df_e_approved["response"].value_counts()

df_e_sga = compares("A.PF.BUDGETSPEND.e.e1.SGA",)
e_sga = df_e_sga["response"].value_counts()

df_e_extra = compares("A.PF.BUDGETSPEND.e.e1.EXTRASPENDING",)
e_extra = df_e_extra["response"].value_counts()

df_e_pubcorp = compares("A.PF.BUDGETSPEND.e.e1.PUBCORP")
e_pubcorp = df_e_pubcorp["response"].value_counts()

df_e_admin = compares("A.PF.BUDGETSPEND.e.e2.ADMIN")
e_admin = df_e_admin["response"].value_counts() 

df_e_econ = compares("A.PF.BUDGETSPEND.e.e2.ECON")
e_econ = df_e_econ["response"].value_counts() 

df_e_func = compares("A.PF.BUDGETSPEND.e.e2.FUNC")
e_func = df_e_func["response"].value_counts() 

df_e_program = compares("A.PF.BUDGETSPEND.e.e2.PROGRAM")
e_program = df_e_program["response"].value_counts() 

df_e_timely = compares("A.PF.BUDGETSPEND.e.e3.TIMELY")
e_timely = df_e_timely["response"].value_counts() 


#new_dataframe = compare("A.PF.BUDGETSPEND.e.e3.FREE",)
#answers = new_dataframe["response"].value_counts()
#print(answers)  

####AVAILABILITY
df_a_online = compare("A.PF.BUDGETSPEND.a.ONLINE",)
a_online = df_a_online["response"].value_counts()

df_a_proposed = compare("A.PF.BUDGETSPEND.e.e1.PROPOSED",)
a_proposed = df_a_proposed["response"].value_counts()

df_a_amended = compare("A.PF.BUDGETSPEND.e.e1.AMENDED",)
a_amended = df_a_amended["response"].value_counts()

df_a_approved = compare("A.PF.BUDGETSPEND.e.e1.APPROVED",)
a_approved = df_a_approved["response"].value_counts()

df_a_sga = compare("A.PF.BUDGETSPEND.e.e1.SGA",)
a_sga = df_a_sga["response"].value_counts()

df_a_extraspending = compare("A.PF.BUDGETSPEND.e.e1.EXTRASPENDING",)
a_extraspending = df_a_extraspending["response"].value_counts()

df_a_socialsecurity = compare("A.PF.BUDGETSPEND.e.e1.SOCIALSECURITY",)
a_socialsecurity = df_a_socialsecurity["response"].value_counts()

df_a_pubcorp = compare("A.PF.BUDGETSPEND.e.e1.PUBCORP",)
a_pubcorp = df_a_pubcorp["response"].value_counts()

df_a_admin = compare("A.PF.BUDGETSPEND.e.e2.ADMIN",)
a_admin = df_a_admin["response"].value_counts()

df_a_econ = compare("A.PF.BUDGETSPEND.e.e2.ECON",)
a_econ = df_a_econ["response"].value_counts()

df_a_func = compare("A.PF.BUDGETSPEND.e.e2.FUNC",)
a_func = df_a_func["response"].value_counts()

df_a_program = compare("A.PF.BUDGETSPEND.e.e2.PROGRAM",)
a_program = df_a_program["response"].value_counts()

df_a_transaction = compare("A.PF.BUDGETSPEND.e.e2.TRANSACTION",)
a_transaction = df_a_transaction["response"].value_counts()

df_a_crosscutting = compare("A.PF.BUDGETSPEND.e.e2.CROSSCUTTING",)
a_crosscutting = df_a_crosscutting["response"].value_counts()

df_a_commonid = compare("A.PF.BUDGETSPEND.e.e2.COMMONID",)
a_commonid = df_a_commonid["response"].value_counts()

df_a_project = compare("A.PF.BUDGETSPEND.e.e2.PROJECT",)
a_project = df_a_project["response"].value_counts()

df_a_free = compare("A.PF.BUDGETSPEND.e.e3.FREE",)
a_free = df_a_free["response"].value_counts()

df_a_license = compare("A.PF.BUDGETSPEND.e.e3.LICENSE",)
a_license = df_a_license["response"].value_counts()

df_a_lang = compare("A.PF.BUDGETSPEND.e.e3.LANG",)
a_lang = df_a_lang["response"].value_counts()

df_a_tools = compare("A.PF.BUDGETSPEND.e.e3.TOOLS",)
a_tools = df_a_tools["response"].value_counts()

df_a_timely = compare("A.PF.BUDGETSPEND.e.e3.TIMELY",)
a_timely = df_a_timely["response"].value_counts()

df_a_historical = compare("A.PF.BUDGETSPEND.e.e3.HISTORICAL",)
a_historical = df_a_historical["response"].value_counts()

df_a_machine = compare("A.PF.BUDGETSPEND.e.e3.MACHINE_READABLE",)
a_machine = df_a_machine["response"].value_counts()

df_a_bulk = compare("A.PF.BUDGETSPEND.e.e3.BULK",)
a_bulk = df_a_bulk["response"].value_counts()

df_a_missing = compare("A.PF.BUDGETSPEND.e.eb.MISSINGDATA",)
a_missing = df_a_missing["response"].value_counts()

df_a_covid = compare("A.PF.BUDGETSPEND.e.eb.COVIDAFFECTED",)
a_covid = df_a_covid["response"].value_counts()

df_a_extent = compare("A.PF.BUDGETSPEND.c.EXTENT",)
a_extent = df_a_extent["response"].value_counts()

#####GOVERNANCE
df_g_exist = compareg("G.PF.PUB-FINANCE.a.EXIST",)
g_exist = df_g_exist["response"].value_counts()

df_g_datarules = compareg("G.PF.PUB-FINANCE.a.DATARULES",)
g_datarules = df_g_datarules["response"].value_counts()

df_g_summary = compareg("G.PF.PUB-FINANCE.e.e1.SUMMARY",)
g_summary = df_g_summary["response"].value_counts()

df_g_transactions = compareg("G.PF.PUB-FINANCE.e.e1.TRANSACTIONS",)
g_transactions = df_g_transactions["response"].value_counts()

df_g_execbudget = compareg("G.PF.PUB-FINANCE.e.e1.EXECBUDGET",)
g_execbudget = df_g_execbudget["response"].value_counts()

df_g_enacted = compareg("G.PF.PUB-FINANCE.e.e1.ENACTED",)
g_enacted = df_g_enacted["response"].value_counts()

df_g_inyear = compareg("G.PF.PUB-FINANCE.e.e1.INYEAR",)
g_inyear = df_g_inyear["response"].value_counts()

df_g_yer = compareg("G.PF.PUB-FINANCE.e.e1.YER",)
g_yer = df_g_yer["response"].value_counts()

df_g_agency = compareg("G.PF.PUB-FINANCE.e.e2.AGENCY",)
g_agency = df_g_agency["response"].value_counts()

df_g_verification = compareg("G.PF.PUB-FINANCE.e.e2.VERIFICATION",)
g_verification = df_g_verification["response"].value_counts()

df_g_timely = compareg("G.PF.PUB-FINANCE.e.e3.TIMELY",)
g_timely = df_g_timely["response"].value_counts()

df_g_structured = compareg("G.PF.PUB-FINANCE.e.e3.STRUCTURED",)
g_structured = df_g_structured["response"].value_counts()

df_g_extent = compareg("G.PF.PUB-FINANCE.c.EXTENT",)
g_extent = df_g_extent["response"].value_counts()

