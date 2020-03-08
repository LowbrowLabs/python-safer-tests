from safer import CompanySnapshot

us_dot_known_good = 698887
us_dot_known_inactive = 22
us_dot_known_none = 2

mc_mx_known_good = 146894
mc_mx_known_inactive = 22
mc_mx_known_none = 2

name_known_good = 'python'
name_known_bad = 'asdf'

def run_usdot_test(var):
    client = CompanySnapshot()
    company = client.get_by_usdot_number(var)
    print(company.to_json())

def run_mc_mx_test(var):
    client = CompanySnapshot()
    company = client.get_by_mc_mx_number(var)
    print(company.to_json())

def run_by_name(var): 
    client = CompanySnapshot()
    results = client.search(var)
    for company in results:
        print(company)

#Just comment out which tests you don't want to run.
try:
    #run_usdot_test(us_dot_known_none)
    run_mc_mx_test(mc_mx_known_good)
    #run_by_name('asdf')
except Exception as TheError:
    print(TheError)