def carga():
    urlpage = "https://dolarhoy.com/"
    page = requests.get(urlpage)
    soup = BeautifulSoup(page.text, 'html.parser')
    valor = soup.find_all(class_="val")
    cotizaciones = {"blue_c":valor[0].text, "blue_v":valor[1].text, "ofi_c":valor[4].text, "ofi_v":valor[5].text, 
                    "mep_c":valor[6].text, "mep_v":valor[7].text, "ccl_c":valor[8].text, "ccl_v":valor[9].text, 
                    "cripto_c":valor[10].text, "cripto_v":valor[11].text}
    database1 = pd.DataFrame.from_dict(cotizaciones, orient ='index')
    database1.columns =[datetime.now()]
    #return test in cosas
    return(database1)