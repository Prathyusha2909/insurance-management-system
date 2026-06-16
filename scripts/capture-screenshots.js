const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const screenshotsDir = path.resolve(__dirname, '..', 'docs', 'screenshots');
  if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir, { recursive: true });
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  const pages = [
    { url: 'http://localhost:8080/swagger-ui.html', file: 'swagger-ui.png' },
    { url: 'http://localhost:8080/index.html', file: 'premium-calculator.png' },
    { url: 'http://localhost:8080/premium-calculator.html', file: 'premium-calculator.png' },
    { url: 'http://localhost:8080/claim-submission.html', file: 'claim-submission.png' },
    { url: 'http://localhost:8080/admin-dashboard.html', file: 'admin-reports.png' },
    { url: 'http://localhost:8080/soap/premiumCalculator.wsdl', file: 'soap-wsdl.png' },
  ];

  for (const item of pages) {
    console.log(`Capturing ${item.url} -> ${item.file}`);
    await page.goto(item.url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(1000);
    const filePath = path.join(screenshotsDir, item.file);
    await page.screenshot({ path: filePath, fullPage: true });
  }

  await browser.close();
  console.log('Screenshots saved.');
})();
