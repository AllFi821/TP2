import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.infinite_scroll_page import InfiniteScrollPage

driver = webdriver.Chrome()

def run_tp2():
    try:
        # --- PARTIE 1 : DYNAMIC CONTROLS ---
        print("\n--- Phase 1: Dynamic Controls ---")
        dc_pg = DynamicControlsPage(driver)
        dc_pg.load()
        
        assert dc_pg.wait_for_element(dc_pg.CHECKBOX)
        dc_pg.click_remove_add()
        
        # On attend la disparition (Tâche 5)
        assert dc_pg.wait_for_invisibility(dc_pg.CHECKBOX)
        print("[OK] Checkbox a disparu.")

        # Enable / Disable (Tâche 10-14)
        assert not dc_pg.is_input_enabled()
        dc_pg.click_enable_disable()
        
        # On attend que le champ devienne actif
        dc_pg.wait.until(lambda d: dc_pg.is_input_enabled())
        field = driver.find_element(*dc_pg.INPUT_FIELD)
        field.send_keys("Selenium Test")
        assert field.get_attribute("value") == "Selenium Test"
        print("[OK] Champ activé et texte saisi.")

        # --- PARTIE 2 : DYNAMIC LOADING ---
        print("\n--- Phase 2: Dynamic Loading ---")
        dl_pg = DynamicLoadingPage(driver)
        dl_pg.load()
        dl_pg.click_start()
        
        # Attente de l'élément qui n'existe pas encore dans le DOM
        result = dl_pg.wait_for_element(dl_pg.FINISH_TEXT)
        assert result.text == "Hello World!"
        print("[OK] Contenu dynamique chargé : Hello World!")

        # --- PARTIE 4 : INFINITE SCROLL ---
        print("\n--- Phase 4: Infinite Scroll ---")
        scroll_pg = InfiniteScrollPage(driver)
        scroll_pg.load()
        
        initial_count = scroll_pg.get_blocks_count()
        scroll_pg.scroll_down()
        time.sleep(1) # Petit temps pour le chargement JS du scroll
        scroll_pg.scroll_down()
        
        final_count = scroll_pg.get_blocks_count()
        assert final_count > initial_count
        print(f"[OK] Scroll réussi : {initial_count} -> {final_count} blocs.")

    except Exception as e:
        print(f"\n[ERREUR] : {e}")
        driver.save_screenshot("erreur_tp2.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tp2()