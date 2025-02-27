

from common_lib import download_by_link, run_file_exe, connect_app, download_and_execute, check_program_installed, \
    click_object, click_without_title


def Genshin_Impact(app_name, file_name_exe, download_link):
    try:
        #Check app is installed
        result = check_program_installed('HoYoPlay')
        if result:
            return result

        #Download and execute install file
        download_result = download_and_execute(file_name_exe, download_link, 30, 5)

        #If download and excute fail -> return fail
        if not download_result:
            return download_result

        # Connect app
        target_window = connect_app('HoYoPlay Install Program')
        #Click checkbox
        click_without_title(target_window, "MainWindow.frmMain.stackedWidget.pageInstallOverSea.frmBg.bottomFrame.verticalLayoutWidget.frame.serviceCheckBox", 'CheckBox')
        click_without_title(target_window, "MainWindow.frmMain.stackedWidget.pageInstallOverSea.frmBg.bottomFrame.verticalLayoutWidget.frame_2.privacyCheckBox", 'CheckBox')

        # #Click install
        click_object(target_window, 'Quick Installation', 'MainWindow.frmMain.stackedWidget.pageInstallOverSea.frmBg.horizontalLayoutWidget_3.Main.buttonFrame.quickInstall', 'Button')
        click_object(target_window, 'Finish & Launch', 'MainWindow.frmMain.stackedWidget.pageInstallOver.frmBg.frame.btnRun', 'Button')
        # wait install
        sleep(10)

        #Check app is installed
        result = check_program_installed('HoYoPlay')
        return result
    except Exception as e:
        print(f'error install: {e}')
        return False
