/**
 * Google Apps Script for Contact Form to Google Sheets Integration
 * 
 * SETUP INSTRUCTIONS:
 * 
 * 1. Create a new Google Sheet:
 *    - Go to https://sheets.google.com
 *    - Create a new spreadsheet
 *    - Name it "Portfolio Contact Form Responses" (or any name you prefer)
 *    - In the first row (Row 1), add these headers:
 *      A1: Timestamp
 *      B1: Name
 *      C1: Email
 *      D1: Subject
 *      E1: Message
 * 
 * 2. Open Google Apps Script:
 *    - In your Google Sheet, go to Extensions > Apps Script
 *    - Delete any default code and paste this entire script
 * 
 * 3. Deploy as Web App:
 *    - Click "Deploy" > "New deployment"
 *    - Click the gear icon next to "Select type" and choose "Web app"
 *    - Set the following:
 *      Description: "Contact Form Handler"
 *      Execute as: "Me"
 *      Who has access: "Anyone" (this allows your website to submit data)
 *    - Click "Deploy"
 *    - Copy the Web App URL that appears
 * 
 * 4. Update your HTML file:
 *    - Open index.html
 *    - Find the line: const scriptURL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
 *    - Replace 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE' with the Web App URL you copied
 *    - Save the file
 * 
 * 5. Test the form:
 *    - Open your website
 *    - Fill out and submit the contact form
 *    - Check your Google Sheet to see if the data appears
 * 
 * NOTE: The first time you deploy, you may need to authorize the script.
 * Google will prompt you to review permissions - click "Review Permissions"
 * and then "Advanced" > "Go to [Your Project Name] (unsafe)" if needed.
 */

function doPost(e) {
  try {
    // Get the active spreadsheet
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Parse the JSON data from the POST request
    const data = JSON.parse(e.postData.contents);
    
    // Prepare the row data
    const rowData = [
      data.timestamp || new Date().toISOString(),
      data.name || '',
      data.email || '',
      data.subject || '',
      data.message || ''
    ];
    
    // Append the row to the sheet
    sheet.appendRow(rowData);
    
    // Return a success response
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'success',
      'message': 'Data saved successfully'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    // Return an error response
    return ContentService.createTextOutput(JSON.stringify({
      'status': 'error',
      'message': error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Optional: Test function to verify the script works
 * Run this from the Apps Script editor to test
 */
function testFunction() {
  const testData = {
    timestamp: new Date().toISOString(),
    name: 'Test User',
    email: 'test@example.com',
    subject: 'Test Subject',
    message: 'This is a test message'
  };
  
  const mockEvent = {
    postData: {
      contents: JSON.stringify(testData)
    }
  };
  
  const result = doPost(mockEvent);
  Logger.log(result.getContent());
}

