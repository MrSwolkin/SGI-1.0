#!/usr/bin/env python3
"""
Manual E2E test for SGI Assets - Testing from /ativos/ directly
Since login redirect is broken, we'll manually navigate to assets
"""

import time
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        print("=== Manual Assets Test (Post-Login) ===\n")

        # Use existing test user
        test_email = "test@sgi.com"
        test_password = "ComplexPassword123!@#"

        print(f"Using test credentials:")
        print(f"  Email: {test_email}")
        print(f"  Password: {test_password}\n")

        # Step 1: Login
        print("Step 1: Logging in...")
        page.goto("http://localhost:8000/login/")
        page.wait_for_load_state('networkidle')

        page.locator('input[name="username"]').fill(test_email)
        page.locator('input[name="password"]').fill(test_password)
        page.locator('button[type="submit"]').click()
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        print(f"  Current URL: {page.url}\n")

        # Step 2: Navigate directly to assets (workaround for broken redirect)
        print("Step 2: Navigating to /ativos/...")
        page.goto("http://localhost:8000/ativos/")
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        page.screenshot(path="manual_01_assets_list.png", full_page=True)
        print("  ✓ Screenshot: manual_01_assets_list.png")

        # Check for "Novo Ativo" button
        novo_ativo = page.locator('a:has-text("Novo Ativo")')
        if novo_ativo.count() > 0:
            print("  ✓ 'Novo Ativo' button found\n")
        else:
            print("  ✗ 'Novo Ativo' button NOT found\n")
            # Try to find what's on the page
            print("  Page content preview:")
            print(f"    Title: {page.title()}")
            links = page.locator('a').all()
            print(f"    Found {len(links)} links")

        # Step 3: Click to create new asset
        print("Step 3: Clicking 'Novo Ativo'...")
        if novo_ativo.count() > 0:
            novo_ativo.click()
            page.wait_for_load_state('networkidle')
            time.sleep(1)

            page.screenshot(path="manual_02_asset_form.png", full_page=True)
            print("  ✓ Screenshot: manual_02_asset_form.png")
            print(f"  Current URL: {page.url}\n")

            # Step 4: Fill form
            print("Step 4: Filling asset form...")

            # Ticker
            ticker_field = page.locator('input[name="ticker"]')
            if ticker_field.count() > 0:
                ticker_field.fill("VALE3")
                print("  ✓ Ticker: VALE3")

            # Name
            name_field = page.locator('input[name="name"]')
            if name_field.count() > 0:
                name_field.fill("Vale ON")
                print("  ✓ Name: Vale ON")

            # Asset type
            type_field = page.locator('select[name="asset_type"]')
            if type_field.count() > 0:
                type_field.select_option(value="STOCK")
                print("  ✓ Type: STOCK (Ação)")
            else:
                print("  ✗ Asset type field not found")

            # Currency
            currency_field = page.locator('select[name="currency"]')
            if currency_field.count() > 0:
                currency_field.select_option(value="BRL")
                print("  ✓ Currency: BRL")
            else:
                print("  ✗ Currency field not found")

            time.sleep(0.5)
            page.screenshot(path="manual_03_form_filled.png", full_page=True)
            print("  ✓ Screenshot: manual_03_form_filled.png\n")

            # Step 5: Submit
            print("Step 5: Submitting form...")
            submit_btn = page.locator('button[type="submit"]')
            if submit_btn.count() > 0:
                submit_btn.click()
                page.wait_for_load_state('networkidle')
                time.sleep(1)

                print(f"  Current URL: {page.url}")
                page.screenshot(path="manual_04_after_submit.png", full_page=True)
                print("  ✓ Screenshot: manual_04_after_submit.png\n")

                # Step 6: Verify asset in list
                print("Step 6: Verifying asset appears...")

                content = page.content()

                if 'VALE3' in content:
                    print("  ✓ Asset 'VALE3' found on page")
                else:
                    print("  ✗ Asset 'VALE3' NOT found")

                if 'Vale ON' in content:
                    print("  ✓ Asset name 'Vale ON' found on page")
                else:
                    print("  ✗ Asset name 'Vale ON' NOT found")

                # Check for success message
                if 'sucesso' in content.lower() or 'cadastrado' in content.lower():
                    print("  ✓ Success message detected")
                else:
                    print("  ℹ No clear success message")

                # Check table structure
                print("\nStep 7: Analyzing table...")
                table = page.locator('table')
                if table.count() > 0:
                    print("  ✓ Table found")

                    # Headers
                    headers = page.locator('th').all_text_contents()
                    print(f"  Headers: {headers}")

                    # Rows
                    rows = page.locator('tbody tr')
                    print(f"  Rows: {rows.count()}")

                    if rows.count() > 0:
                        # Get all cells from first row
                        first_row = rows.first
                        cells = first_row.locator('td').all_text_contents()
                        print(f"  First row: {cells}")
                else:
                    print("  ℹ No table found")

                page.screenshot(path="manual_05_final.png", full_page=True)
                print("\n  ✓ Screenshot: manual_05_final.png")
            else:
                print("  ✗ Submit button not found")

        print("\n=== Test Complete ===")
        print("Keep browser open for inspection? (5 sec)")
        time.sleep(5)

        browser.close()

if __name__ == "__main__":
    run_test()
