function detectOS() {
  const ua = navigator.userAgent;
  const platform = navigator.userAgentData?.platform || navigator.platform || '';
  if (/Windows/i.test(platform) || /Windows/i.test(ua)) return 'Windows';
  if (/Mac/i.test(platform) || /Mac/i.test(ua)) return 'macOS';
  if (/Android/i.test(ua)) return 'Android';
  if (/iPhone|iPad|iPod/i.test(ua)) return 'iOS';
  if (/Linux/i.test(platform) || /Linux/i.test(ua)) return 'Linux';
  return "OS I didn't account for";
}

const osParagraph = document.createElement('p');
osParagraph.textContent = "Hello " + detectOS() + " user!";
osParagraph.style.fontSize = "2em";
osParagraph.style.fontWeight = "bold";
osParagraph.style.lineHeight = "1.2";
osParagraph.style.margin = "0";
document.body.prepend(osParagraph);
