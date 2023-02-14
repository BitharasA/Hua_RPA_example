from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

# navigate to the Yahoo Mail login page

driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://mail.yahoo.com/")

time.sleep(5)
driver.set_page_load_timeout(5)
webdriver.Chrome.implicitly_wait(driver, 10)

# enter your Yahoo email address
username = driver.find_element(By.ID, "login-username")
username.send_keys("xxxxxxx@xxxxxx")
username.send_keys(Keys.RETURN)
driver.set_page_load_timeout(2)
time.sleep(2)
driver.implicitly_wait(20)
driver.set_page_load_timeout(2)

####Enter your Yahoo password

password = driver.find_element(By.ID, "login-passwd")
password.send_keys("xxxxxxxxx")
password.send_keys(Keys.RETURN)
time.sleep(15)

####Search the given password

searchfield = driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/div[2]/div/div/div/div[1]/ul/li/div/div/input[1]')
searchfield.send_keys('subject:VM-Creation is:unread')
searchfield.send_keys(Keys.RETURN)
time.sleep(10)

####Open e-mail and export the VM specs

emails = driver.find_element(By.CSS_SELECTOR, "html#Atom body.bold-focus.pointer-mode div#mail-app-container div.pointer-mode.H_6D6F div.D_F.ek_BB.H_6D6F.aw_2941hk.ba_10I1Qt.az_oOItw.ay_Z1nkUQx.I_kt4zd div#app.D_F.ek_BB.H_6D6F.cZ1RN91d_n.s_1HCsWR.aw_Z22yhkg.I_kt4zd.az_DW.ba_Z2gmOa3.ay_Z1cYiMT.c2hBT4u_Zm6i39.cZTwBjO_Zdogtk div.I_ZS20V7.D_F.em_N.o_h.W_6D6F.H_6D6F div.D_F.em_N.o_h.s_1HCsWR div#mail-app-component-container.D_F.em_N.ej_eUh.o_h div#mail-app-component.em_N.gl_C.I_29psyX.j_n.o_h.p_R.D_F.s_e5X.x_ZYfqDw div.em_N.gl_C.o_h.D_F.p_R.U_0 div.W_6D6F.D_F div.D_F.ab_FT.em_N.ek_BB.W_6D6F div.D_F.ab_FT.em_N.ek_BB.iz_A.H_6D6F div.D_F.H_6D6F.ab_FT.em_N.p_R.M_0 div.D_F.ek_BB.W_6D6F div.W_6D6F.H_6D6F.cZ1RN91d_n.o_h.p_R.em_N.D_F div.p_R.o_h.D_F.H_A.W_6D6F.k_w.em_N div.p_R.Z_0.iy_h.iz_A.W_6D6F.H_6D6F.k_w.em_N.c22hqzz_GN ul.M_0.P_0 li.H_A.hd_n.p_a.L_0.R_0 a.D_B.bn_dBP.bm_FJ.bj_a0xJ8.I4_1YEmYj.C_ZpQYvz.is_26ISAR.cZdTOHS_ZXgLQ3 div.D_F.r_P.ab_C.p_R.A_6EqO.i_6FIA.c1AVi73_6FsP.c1AVi7H_6LEV.o_h.X_eo6.Y_eo6.C_ZnIF8Y.message-list-item div.D_F.o_h.ab_C.H_6D6F.em_sL.ej_0 div.D_F.ab_C.o_h.H_6D6F.em_N.E_fq7.J_x div.en_3ixhM.o_h.a_6D6F.D_F.ab_C span.en_N.u_Z13VSE6.o_h.G_e.J_x span.I_Z1gjd5v.D_X.P_3zDxc.I_a0xJ8")
emails.click()
time.sleep(10)
emailtext = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li/div/div[2]/div[1]/div[2]/div/div/div/div/div/div").text

lines = emailtext.split("\n")

for line in lines:
    if "VM size:" in line:
        vm_size = line.split(":")[1]
    if "VM name" in line:
        vm_name = line.split(":")[1]
    if "Region" in line:
        vm_region = line.split(":")[1]
        break
    
print(vm_size)
print(vm_name)
print(vm_region)
time.sleep(1)

####Open portal.azure.com in a new tab

driver.execute_script("window.open('https://portal.azure.com' , '_blank');")
time.sleep(8)
driver.switch_to.window(driver.window_handles[1]) #Chooses the current tab for the context

#####Enter Azure Portal 

AzureUsername = driver.find_element(By.NAME, "loginfmt")
AzureUsername.send_keys("xxxxxxxx@xxxxxxx")
AzureUsername.send_keys(Keys.RETURN)
time.sleep(4)
AzurePass = driver.find_element(By.NAME, "passwd")
AzurePass.send_keys("xxxxxxxxx")
AzurePass.send_keys(Keys.RETURN)
time.sleep(4)
Connected = driver.find_element(By.ID, "idSIButton9")
Connected.click()
time.sleep(4)

#####Create resource

CreateResource = driver.find_element(By.ID, "_weave_e_49")
CreateResource.click()
time.sleep(2)
CreateVM = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/div/div[2]/a")
CreateVM.click()

#####Resource properties
time.sleep(3)
VMnamefield = driver.find_element(By.NAME, "__azc-textBox-tsx1")
VMnamefield.send_keys(vm_name)
VMnamefield.send_keys(Keys.RETURN)
time.sleep(10)
RegionField = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[10]/div[2]/div/span")
RegionField.click()
time.sleep(3)
RegionSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[10]/div[2]/div/div[2]/div[2]/div/div[1]/div[8]/span")
RegionSelect.click()
time.sleep(2)
AvZonesField = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[12]/div[2]/div/div[1]")
AvZonesField.click()
time.sleep(3)
AvZonesSelect = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[12]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/span/span[1]")
AvZonesSelect.click()
time.sleep(2)

####Select Size
VMSize = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[24]/div[2]/label[1]/div[1]/span/a")
VMSize.click()
time.sleep(3)
VMSizeSelection = driver.find_element(By.NAME, "__azc-textBox-tsx5")
VMSizeSelection.send_keys(vm_size)
time.sleep(3)
Sizeselect2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[3]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div")
Sizeselect2.click()
time.sleep(3)
VMSizeSelectionButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[3]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div/div")
VMSizeSelectionButton.click()
time.sleep(3)

####Next To Disks
NextButtonDisks = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonDisks.click()
time.sleep(3)

####Next To Networking
NextButtonNet = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonNet.click()
time.sleep(3)

####Next To Management
NextButtonManag = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonManag.click()
time.sleep(3)

####Next To Monitoring
NextButtonMon = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonMon.click()
time.sleep(3)

####Next To Advanced
NextButtonAdv = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonAdv.click()
time.sleep(3)

####Next To Tags
NextButtonTag = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonTag.click()
time.sleep(3)

####Next To Tags
NextButtonTag = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]")
NextButtonTag.click()
time.sleep(10)

####Create Button 
CreateButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]")
CreateButton.click()
time.sleep(3)

####Download The SSH Key
SSHDown = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[3]/div[2]/section[2]/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/div/div[1]")
SSHDown.click()

time.sleep(30)
driver.quit()