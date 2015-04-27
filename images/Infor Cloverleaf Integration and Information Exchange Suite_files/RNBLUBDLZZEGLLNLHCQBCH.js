(function () {
  var scheme = (("https:" == document.location.protocol) ? "https" : "http");
  var adnxs_domain = 'secure.adnxs.com';
  var aol_domain = 'secure.leadback.advertising.com';
  var rule = ["*", "*"];
  if (scheme=='http') { adnxs_domain = 'ib.adnxs.com'; aol_domain = 'leadback.advertising.com';}
  var el = document.createElement("div");
  el.style["width"] = "1px";
  el.style["height"] = "1px";
  el.style["display"] = "inline";
  var content = unescape('%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/r/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/f/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/b/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/x/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/l/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/o/out%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//d.adroll.com/cm/g/out%3fgoogle_nid%3dadroll5%22/%3e%0a%3cimg%20height%3d%221%22%20width%3d%221%22%20alt%3d%22%22%20style%3d%22display%3anone%22%20src%3d%22https%3a//www.facebook.com/tr%3fid%3d677147722405849%26cd%5bsegment_eid%5d%3dDGDTFDQWCNEJFK55VPBLPR%26ev%3dNoScript%22%20/%3e%3cimg%20height%3d%221%22%20width%3d%221%22%20style%3d%22border-style%3anone%3b%22%20alt%3d%22%22%20src%3d%22%5bprotocol%5d%3a//googleads.g.doubleclick.net/pagead/viewthroughconversion/0/%3flabel%3dnull%26amp%3bguid%3dON%26amp%3bscript%3d0%26amp%3bord%3d%5bord%5d%22/%3e%0a%3cimg%20src%3d%22%5bprotocol%5d%3a//%5badnxs_domain%5d/seg%3fadd%3d2396817%26t%3d2%22%20width%3d%221%22%20height%3d%221%22/%3e%0a');
  

  try {
  
  } catch(e) {}

  var r = Math.random()*10000000000000000;
  content = content.replace(/\[ord\]/gi, r);
  content = content.replace(/\[protocol\]/gi, scheme);
  content = content.replace(/\[adnxs_domain\]/gi, adnxs_domain);
  content = content.replace(/\[aol_domain\]/gi, aol_domain);
  content = __adroll.replace_external_data(content);
  el.innerHTML = content;
  __adroll._head().appendChild(el);
  if (typeof __adroll.set_pixel_cookie != 'undefined') {__adroll.set_pixel_cookie(adroll_adv_id, adroll_pix_id, "DGDTFDQWCNEJFK55VPBLPR");}
}());
