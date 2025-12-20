# Google Sheets Integration Setup Guide

This guide will help you set up the contact form to automatically save submissions to a Google Sheet.

## Step 1: Create a Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it "Portfolio Contact Form Responses" (or any name you prefer)
4. In the first row (Row 1), add these column headers:
   - **Column A**: Timestamp
   - **Column B**: Name
   - **Column C**: Email
   - **Column D**: Subject
   - **Column E**: Message

## Step 2: Set Up Google Apps Script

1. In your Google Sheet, click **Extensions** > **Apps Script**
2. Delete any default code in the editor
3. Copy the entire contents of `google-sheets-setup.js` and paste it into the Apps Script editor
4. Click **Save** (or press Ctrl+S / Cmd+S)
5. Give your project a name (e.g., "Contact Form Handler")

## Step 3: Deploy as Web App

1. Click **Deploy** > **New deployment**
2. Click the gear icon (⚙️) next to "Select type" and choose **Web app**
3. Configure the deployment:
   - **Description**: "Contact Form Handler"
   - **Execute as**: "Me" (your email)
   - **Who has access**: **"Anyone"** (this is important - it allows your website to submit data)
4. Click **Deploy**
5. **Copy the Web App URL** that appears (it will look like: `https://script.google.com/macros/s/...`)

## Step 4: Update Your HTML File

1. Open `index.html` in your code editor
2. Find this line (around line 1970):
   ```javascript
   const scriptURL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
   ```
3. Replace `'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE'` with the Web App URL you copied in Step 3
4. Save the file

## Step 5: Authorize the Script (First Time Only)

1. The first time you deploy, Google will ask you to authorize the script
2. Click **Review Permissions**
3. Select your Google account
4. You may see a warning that the app isn't verified - this is normal for personal scripts
5. Click **Advanced** > **Go to [Your Project Name] (unsafe)**
6. Click **Allow** to grant permissions

## Step 6: Test the Form

1. Open your website in a browser
2. Fill out the contact form with test data
3. Submit the form
4. Check your Google Sheet - you should see the data appear in a new row

## Troubleshooting

### Form submissions aren't appearing in the sheet:
- Verify the Web App URL is correct in `index.html`
- Check that the Web App deployment has "Who has access" set to "Anyone"
- Make sure you've authorized the script (Step 5)
- Check the Apps Script execution log for errors (View > Executions)

### Getting CORS errors:
- The `mode: 'no-cors'` in the fetch request should handle this, but if you see errors, make sure the Web App URL is correct

### Need to update the script:
- After making changes to the Apps Script code, you need to create a **new deployment** (Deploy > Manage deployments > Edit > New version > Deploy)

## Security Note

The current setup allows anyone to submit data to your sheet. This is fine for a contact form, but if you want to add additional security:
- You can add a simple token/secret key check in the Apps Script
- Or use Google Forms with a more restricted setup

## Alternative: Using Google Forms

If you prefer a simpler setup without coding, you can:
1. Create a Google Form
2. Get the form's action URL
3. Update the HTML form to submit directly to the Google Form URL

However, the current Apps Script method gives you more control over the data format and allows for custom styling.

