from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del controlador de Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Para abrir el navegador maximizado

# Inicializar el controlador de Chrome
driver = webdriver.Chrome(options=options)

try:
    # Abrir la página de Yahoo en español
    driver.get("https://espanol.yahoo.com/")

    # Esperar a que el campo de búsqueda esté disponible y realizar una búsqueda
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "p"))
    )
    search_box.send_keys("noticias de hoy en México")
    search_box.send_keys(Keys.RETURN)

    # Esperar a que los resultados de búsqueda aparezcan
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "web"))
    )

    # Encontrar el enlace a la sección de noticias y hacer clic en él
    news_section = driver.find_element(By.PARTIAL_LINK_TEXT, "Noticias")
    news_section.click()

    # Esperar a que la sección de noticias cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )

    print("Navegación completada y sección de noticias cargada.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Mantener el navegador abierto
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
