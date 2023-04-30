import mechanize 

def viewPage(url):
    browser = mechanize.Browser() 
    browser.set_handle_robots(False)
    page = browser.open(url)
    print("*" * 16 + " PAGE HTML " + "*" * 16)
    source_code = page.read() 
    print (source_code)
    print("*" * 16 + " END PAGE HTML " + "*" * 16)
    print("*" * 16 + " FORM " + "*" * 16)
    browser.select_form(name="form1") 
    print (browser.form)
    print("*" * 16 + " END FORM " + "*" * 16)
    
viewPage('http://testphp.vulnweb.com/signup.php')