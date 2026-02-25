#!/usr/bin/env python3
"""
Automated E2E test for SGI Assets app using Playwright
Tests the complete user flow from registration to asset creation
"""

import time
import random
from playwright.sync_api import sync_playwright, expect

def run_test():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        print("=== Starting SGI Assets App E2E Test ===\n")

        # Generate unique test user credentials
        timestamp = int(time.time())
        test_email = f"test{timestamp}@example.com"
        test_password = "ComplexPassword123!@#"  # Strong password not similar to email
        test_first_name = "João"
        test_last_name = "Silva"

        print(f"Test credentials:")
        print(f"  Email: {test_email}")
        print(f"  Password: {test_password}\n")

        # Step 1: Navigate to registration page
        print("Step 1: Navigating to registration page...")
        page.goto("http://localhost:8000/cadastro/")
        page.wait_for_load_state('networkidle')
        time.sleep(1)
        page.screenshot(path="screenshot_01_register_page.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_01_register_page.png\n")

        # Step 2: Fill registration form
        print("Step 2: Filling registration form...")

        # Fill first name
        first_name_input = page.locator('input[name="first_name"]')
        if first_name_input.count() > 0:
            first_name_input.fill(test_first_name)
            print(f"  ✓ First name: {test_first_name}")

        # Fill last name
        last_name_input = page.locator('input[name="last_name"]')
        if last_name_input.count() > 0:
            last_name_input.fill(test_last_name)
            print(f"  ✓ Last name: {test_last_name}")

        # Fill email
        email_input = page.locator('input[name="email"]')
        email_input.fill(test_email)
        print(f"  ✓ Email: {test_email}")

        # Fill password
        password_input = page.locator('input[name="password1"]')
        password_input.fill(test_password)
        print(f"  ✓ Password: {test_password}")

        # Fill password confirmation
        password_confirm_input = page.locator('input[name="password2"]')
        password_confirm_input.fill(test_password)
        print(f"  ✓ Password confirmation: {test_password}")

        page.screenshot(path="screenshot_02_register_form_filled.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_02_register_form_filled.png\n")

        # Submit registration
        print("Step 3: Submitting registration...")
        submit_button = page.locator('button[type="submit"]')
        submit_button.click()
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        current_url = page.url
        print(f"  Current URL after registration: {current_url}")
        page.screenshot(path="screenshot_03_after_register.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_03_after_register.png\n")

        # Check if we're on login page (successful registration should redirect to login)
        if '/login/' in current_url:
            print("  ✓ Successfully redirected to login page")

            # Step 4: Login
            print("\nStep 4: Logging in with new credentials...")
            email_input = page.locator('input[name="username"]')
            email_input.fill(test_email)

            password_input = page.locator('input[name="password"]')
            password_input.fill(test_password)

            page.screenshot(path="screenshot_04_login_form_filled.png", full_page=True)
            print("  ✓ Screenshot saved: screenshot_04_login_form_filled.png")

            submit_button = page.locator('button[type="submit"]')
            submit_button.click()
            page.wait_for_load_state('networkidle')
            time.sleep(1)
        else:
            print("  ⚠ Not on login page, might be auto-logged in")

        current_url = page.url
        print(f"  Current URL after login: {current_url}")
        page.screenshot(path="screenshot_05_after_login.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_05_after_login.png\n")

        # Step 5: Navigate to assets page
        print("Step 5: Navigating to assets page (/ativos/)...")
        page.goto("http://localhost:8000/ativos/")
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        page.screenshot(path="screenshot_06_assets_list_empty.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_06_assets_list_empty.png")

        # Check for empty state
        page_content = page.content()
        if 'Nenhum ativo' in page_content or 'vazio' in page_content.lower():
            print("  ✓ Empty state detected\n")
        else:
            print("  ℹ Empty state message not clearly visible\n")

        # Step 6: Click "Novo Ativo" button
        print("Step 6: Clicking 'Novo Ativo' button...")

        # Try multiple selectors for the button
        novo_ativo_button = None
        selectors = [
            'a:has-text("Novo Ativo")',
            'button:has-text("Novo Ativo")',
            'a[href*="novo"]',
            'a[href="/ativos/novo/"]'
        ]

        for selector in selectors:
            if page.locator(selector).count() > 0:
                novo_ativo_button = page.locator(selector).first
                print(f"  ✓ Found button using selector: {selector}")
                break

        if novo_ativo_button:
            novo_ativo_button.click()
            page.wait_for_load_state('networkidle')
            time.sleep(1)

            current_url = page.url
            print(f"  Current URL: {current_url}")
            page.screenshot(path="screenshot_07_asset_create_form.png", full_page=True)
            print("  ✓ Screenshot saved: screenshot_07_asset_create_form.png\n")
        else:
            print("  ✗ Could not find 'Novo Ativo' button")
            print("  Available links on page:")
            links = page.locator('a').all()
            for link in links[:10]:
                print(f"    - {link.text_content()}")
            print("\n")

        # Step 7: Fill asset creation form
        print("Step 7: Filling asset creation form...")

        # Ticker
        ticker_input = page.locator('input[name="ticker"]')
        if ticker_input.count() > 0:
            ticker_input.fill("PETR4")
            print("  ✓ Ticker: PETR4")

        # Name
        name_input = page.locator('input[name="name"]')
        if name_input.count() > 0:
            name_input.fill("Petrobras PN")
            print("  ✓ Name: Petrobras PN")

        # Type (select dropdown)
        type_select = page.locator('select[name="asset_type"]')
        if type_select.count() > 0:
            type_select.select_option(label="Ação")
            print("  ✓ Type: Ação")
        else:
            print("  ✗ Type select not found")

        # Currency (select dropdown)
        currency_select = page.locator('select[name="currency"]')
        if currency_select.count() > 0:
            currency_select.select_option(label="Real (BRL)")
            print("  ✓ Currency: Real (BRL)")

        time.sleep(0.5)
        page.screenshot(path="screenshot_08_asset_form_filled.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_08_asset_form_filled.png\n")

        # Step 8: Submit form
        print("Step 8: Submitting asset creation form...")
        submit_button = page.locator('button[type="submit"]')
        submit_button.click()
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        current_url = page.url
        print(f"  Current URL after submission: {current_url}")
        page.screenshot(path="screenshot_09_after_asset_creation.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_09_after_asset_creation.png\n")

        # Step 9: Verify asset appears in list
        print("Step 9: Verifying asset in list...")

        page_content = page.content()

        if 'PETR4' in page_content:
            print("  ✓ Asset ticker 'PETR4' found on page")
        else:
            print("  ✗ Asset ticker 'PETR4' NOT found on page")

        if 'Petrobras PN' in page_content:
            print("  ✓ Asset name 'Petrobras PN' found on page")
        else:
            print("  ✗ Asset name 'Petrobras PN' NOT found on page")

        # Check for success message
        success_indicators = ['sucesso', 'criado', 'adicionado', 'success']
        success_found = any(indicator in page_content.lower() for indicator in success_indicators)

        if success_found:
            print("  ✓ Success message detected")
        else:
            print("  ℹ No clear success message detected")

        # Take final screenshot
        page.screenshot(path="screenshot_10_final_assets_list.png", full_page=True)
        print("  ✓ Screenshot saved: screenshot_10_final_assets_list.png\n")

        # Step 10: Analyze the table structure
        print("Step 10: Analyzing asset table structure...")

        # Check if table exists
        table = page.locator('table')
        if table.count() > 0:
            print("  ✓ Table element found")

            # Check for headers
            headers = page.locator('th').all_text_contents()
            print(f"  Table headers: {headers}")

            # Check for data rows
            rows = page.locator('tbody tr')
            row_count = rows.count()
            print(f"  Data rows found: {row_count}")

            if row_count > 0:
                # Get first row data
                first_row = rows.first
                cells = first_row.locator('td').all_text_contents()
                print(f"  First row data: {cells}")
        else:
            print("  ℹ No table element found, checking for alternative layout...")
            # Check for card-based layout
            cards = page.locator('[class*="card"]')
            if cards.count() > 0:
                print(f"  ✓ Found {cards.count()} card elements")

        print("\n=== Test Complete ===")
        print("All screenshots saved to project root directory")

        # Keep browser open for manual inspection
        print("\nBrowser will stay open for 5 seconds for manual inspection...")
        time.sleep(5)

        browser.close()

if __name__ == "__main__":
    run_test()
