# data_testcase = {
#                 'test case': ['Ahnlab Safe Transaction', 'Alcapture', 'APS Engine', 'CrossWebEX', 'Wizin Delfino G3', 'IPinsideLWS',
#                               'nProtect Online Security'],
#                 'test case detail': ['https://bank.shinhan.com/sw/astx/astxdn.exe',
#                                      'https://advert.estsoft.com/?event=201110311523647',
#                                      'https://mybank.ibk.co.kr/IBK/uib/sw/yettiesoft/APS/APS_Engine.exe',
#                                      'https://bank.shinhan.com/sw/initech/extension/down/INIS_EX_SHA2.exe?ver=1.0.1.961',
#                                      'https://mybank.ibk.co.kr/IBK/uib/sw/wizvera/delfino/down/delfino-g3-sha2.exe',
#                                      'https://mybank.ibk.co.kr/IBK/uib/sw/interezen/agent/I3GSvcManager.exe',
#                                      'https://supdate.nprotect.net/nprotect/nos_service/windows/install/nos_setup.exe']
#             }

app_list_data = [
    ['Ahnlab Safe Transaction', 'https://bank.shinhan.com/sw/astx/astxdn.exe'],
    ['Adobe Acrobat Reader', 'readerdc64_ga_cra_install.exe', 'https://admdownload.adobe.com/rdcm/installers/live/readerdc64_ga_cra_install.exe'],
    ['Adobe Creative Cloud', 'Creative_Cloud_Set-Up.exe', 'https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&guid=d8738952-724a-4ffa-b844-ae8af08d8259&contextParams=%7B%22component%22%3A%22cc-home%22%2C%22visitor_guid%22%3A%2217544139162251472000750151510417531777%22%2C%22campaign_id%22%3A%2245274%7C92568%7C96659%7C2021-10-cme-1%7C2023-09-apps-catalog-M2%22%2C%22browser%22%3A%22chrome%22%2C%22context_guid%22%3A%227d3c1f19-9cdc-4e58-92fc-6c0f2350c3bd%22%2C%22variation_id%22%3A%22130841%3A45274%7C287164%3A92568%7C299138%3A96659%7Ctest%3A2021-10-cme-1%7Ctest%3A2023-09-apps-catalog-M2%22%2C%22experience_id%22%3A%22na%3A45274%7Cna%3A92568%7Cna%3A96659%7Cna%3A2021-10-cme-1%7Cna%3A2023-09-apps-catalog-M2%22%2C%22planCodeList%22%3A%22cc_free%7Cdc_free%22%2C%22updateCCD%22%3A%22true%22%2C%22secondarySapcodeList%22%3A%22%22%2C%22Product_ID_Promoted%22%3A%22KCCC%22%2C%22userGuid%22%3A%22198278505EBCAAC20A495FB4%40AdobeID%22%2C%22authId%22%3A%22198278505EBCAAC20A495FB4%40AdobeID%22%2C%22contextComName%22%3A%22Organic%3ACCH%22%2C%22contextSvcName%22%3A%22NO-CCD%22%2C%22contextOrigin%22%3A%22Organic%3ACCH%22%2C%22AMCV_D6FAAFAD54CA9F560A4C98A5%2540AdobeOrg%22%3A%22-637568504%257CMCIDTS%257C20144%257CMCMID%257C17544139162251472000750151510417531777%257CMCAAMLH-1741061086%257C3%257CMCAAMB-1741061086%257C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%257CMCOPTOUT-1740463486s%257CNONE%257CMCSYNCSOP%257C411-20147%257CvVersion%257C5.1.1%22%2C%22mid%22%3A%2222233660565938630591820048530096679807%22%2C%22aid%22%3A%22%22%2C%22AppMeasurementVersion%22%3A%222.23.0%22%2C%22kaizenTrialDuration%22%3A7%7D&wamFeature=nuj-live&environment=prod&api_key=CCHomeWeb1'],
    ['Alcapture', 'https://advert.estsoft.com/?event=201110311523647', 'https://creativecloud.adobe.com/apps/download/creative-cloud'],
    ['APS Engine', 'APS_Engine.exe', 'https://mybank.ibk.co.kr/IBK/uib/sw/yettiesoft/APS/APS_Engine.exe'],
    ['CrossWebEX', 'INIS_EX_SHA2.exe', 'https://bank.shinhan.com/sw/initech/extension/down/INIS_EX_SHA2.exe?ver=1.0.1.961'],
    ['Wizin Delfino G3', 'https://mybank.ibk.co.kr/IBK/uib/sw/wizvera/delfino/down/delfino-g3-sha2.exe'],
    ['IPinsideLWS', 'https://mybank.ibk.co.kr/IBK/uib/sw/interezen/agent/I3GSvcManager.exe'],
    ['Printmade', 'Printmade3_setup.exe', 'https://bank.shinhan.com/sw/printmade/download_files/Windows/Printmade3_setup.exe'],
    ['TouchEnNxKey', 'TouchEn_nxKey_32bit.exe', 'https://bank.shinhan.com/sw/raon/TouchEn/nxKey/module/TouchEn_nxKey_32bit.exe?ver=1.0.0.8'],
    ['Bandizip', 'BANDIZIP-SETUP-STD-X64.EXE', 'https://kr.bandisoft.com/bandizip/dl.php?web'],
    ['Gom Audio', 'GOMAUDIOGLOBALSETUP_NEW.EXE', 'https://cdn2.gomlab.com/gretech/audio/GOMAUDIOGLOBALSETUP_NEW.EXE'],
    ['Alsong', 'ALSong352.exe', 'https://advert.estsoft.com/?event=200803271705239'],
    ['Melon Player', 'MelonSetup.exe', 'https://cdnstatic.melon.co.kr/svc/pcp/apps/w10/MelonSetup.exe'],
    ['Dropbox', 'DropboxInstaller.exe', 'https://dl-web.dropbox.com/installer?arch=x86_64&authenticode_sign=True&build_no=218.4.4348&juno=True&juno_use_program_files=True&omaha=True&omaha_use_program_files=True&plat=win&tag=eyJUQUdTIjoiZUp5clZpcE9MUzdPek0tTHoweFJzbEl3TlRFeE1qSXl0ekN4TkRNM05UQTB0REEwTVRJek1EUTFNalcyTkRRMU1ESTBOTFUwTnFvRkFKc1VEWFV-QE1FVEEifQ&tag_token=AgSUCkxdvsAaMv3mTcZhPII-gCEHcXYf7IqCPIGb8yzwdA'],
    ['Evermote', 'Evernote-latest.exe', 'https://win.desktop.evernote.com/builds/Evernote-latest.exe'],


                ]
