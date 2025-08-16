
<!DOCTYPE html><html lang="en"><head>
  <meta charset="utf-8">
  <title>MobileShop.com</title>
  <link rel="icon" type="image/x-icon" href="https://imgs.tamildating.com/bmimages/faviconnew.ico">
  <base href="/main/"> 
  <meta name="color-scheme" content="light dark">
  <meta name="viewport" content="viewport-fit=cover, width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <meta name="format-detection" content="telephone=no">
  <meta name="msapplication-tap-highlight" content="no">
    <!-- add to homescreen for ios -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <script src="assets/js/firebaseConfig.js"></script>
  <script src="assets/js/pwa-events.js"></script>
  <script src="https://www.gstatic.com/firebasejs/7.17.2/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/7.17.2/firebase-analytics.js"></script>
  <script src="https://www.gstatic.com/firebasejs/7.17.2/firebase-messaging.js"></script>

  <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>


<script>
  var title = ["speaking people", "Kannadigas", "Malayalis", "Odias"];
  var hname = window.location.hostname.split(".");
    if (hname[1] != undefined) {
      var dname = hname[1] && hname[1].replace("dating", "");
      var uppercasedname = dname.toUpperCase();
      var dname_mt = dname.substr(1);
      var domain_mt = uppercasedname[0] + dname_mt;
    } else {
      var domain_mt = "Tamil";
    }

    if(dname!=undefined){
      var strlink = '<link rel="manifest" href="' + dname + '-manifest.json">';
      document.write(strlink);
    }

    var TitleName = '';
    if (domain_mt == 'Hindi' || domain_mt == 'Urdu') {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + domain_mt + ' ' + title[0] + ' - ' +
        domain_mt + 'Matrimony.com';
    } else if (domain_mt == 'Kannada') {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + title[1] + ' - ' + domain_mt +
        'Matrimony.com';
    } else if (domain_mt == 'Kerala') {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + title[2] + ' - ' + domain_mt +
        'Matrimony.com';
    } else if (domain_mt == 'Oriya') {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + title[3] + ' - ' + domain_mt +
        'Matrimony.com';
    } else if (domain_mt == 'Mobileshop') {
      TitleName = domain_mt + ' Matrimony - The No. 1 & Most Trusted Indian Matrimonial Website - ' + domain_mt +
        'Matrimony.com';
    } else if (domain_mt == 'Assamese') {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + domain_mt + ' - ' + domain_mt +
        'Matrimony.com';
    } else {
      TitleName = domain_mt + ' Matrimony - The No. 1 Matrimony Site for ' + domain_mt + 's - ' + domain_mt +
        'Matrimony.com';
    }
    document.title = TitleName;

    // MetaContent
    var MetaContent = '';
    if (domain_mt == 'Mobileshop') {
      MetaContent =
        'MobileShop - The No. 1 & Most Trusted Matrimony Service for Indians. Millions of success stories. Register Free to find your Perfect Match';
    } else if (domain_mt == 'Parsi') {
      MetaContent = domain_mt + 'Matrimony - The No. 1 & most successful ' + domain_mt +
        ' Matrimonial Site from MobileShop. Trusted by thousands of ' + domain_mt +
        ' Brides & Grooms globally. Register Free!';
    } else {
      MetaContent = domain_mt + 'Matrimony - The No. 1 & most successful ' + domain_mt +
        ' Matrimonial Site from MobileShop. Trusted by lakhs of ' + domain_mt +
        ' Brides & Grooms globally. Register Free!';
    }
    var meta = document.createElement('meta');
    meta.setAttribute('name', 'description');
    meta.content = MetaContent;
    document.getElementsByTagName('head')[0].appendChild(meta);

    window.addEventListener('pageshow', function (event) {
      if (event.persisted || performance.getEntriesByType("navigation")[0].type === 'back_forward') {
        var customEvent = new Event('backFromExternalSite');
        document.dispatchEvent(customEvent);
       }
    });
</script>  

<script>
  //To close the desktop promo popup
function promoClose() {
  my.namespace.publicFunc();
}

function newpromoClose() {
  my.namespace.publicFunc();
}

function getLoggedUserName() {

  var _details = localStorage.getItem("USER_DETAILS");
  if (_details) {
    try {
      var _detailJson = JSON.parse(_details);
      if (_detailJson && _detailJson.name) {
        return _detailJson.name;
      }

    } catch (err) {}
  }

  var _info = localStorage.getItem("USER_INFO_DETAILS");
  if (_info) {
    try {
      var _infoJson = JSON.parse(_info);
      if (_infoJson && _infoJson.name) {
        return _infoJson.name;
      }

    } catch (err) {}
  }

  return localStorage.getItem("NAME") || "";
}

</script>

<script>
  var setinterval = setInterval(function(){
  $matriid = localStorage.getItem("MATRIID");
  $name = localStorage.getItem("NAME");
  if($matriid && $matriid != 'undefined' && $matriid != undefined && $matriid != '') {
  clearInterval(setinterval);
    (function (d, w, c) {
      if (!d.getElementById("spd-busns-spt")) {
        var n = d.getElementsByTagName('script')[0],
          s = d.createElement('script');
        var loaded = false;
        s.id = "spd-busns-spt";
        s.async = "async";
          s.setAttribute("data-self-init", "false");
          s.setAttribute("data-init-type", "normal");
        s.src = 'https://cdn.in-freshbots.ai/assets/share/js/freshbots.min.js';
        s.setAttribute("data-client", "3c81a00513a206b17584c5c6728ba8ecb269b5cf");
        s.setAttribute("data-bot-hash", "427a28b61cc050913962a0a4fa141b700c4d24a3");
        s.setAttribute("data-env", "");
        s.setAttribute("data-region", "in");
        if (c) {
          s.onreadystatechange = s.onload = function () {
            if (!loaded) {
              c();
            }
            loaded = true;
          };
        }
        n.parentNode.insertBefore(s, n);
      }
    })(document, window, function () {
        Freshbots.initiateWidget({
          autoInitChat: false,
          getClientParams: function () {
            return {
              "Matriid": $matriid,
              "cstmr::nm" : getLoggedUserName(),
              "source" : "Desktop"
            };
          }
        }, function (successResponse) {}, function (errorResponse) {});
    });
  }
}, 3000);

function openchatbot() {
  document.getElementById("mobile-chat-container").click();
}

function openAlbumView(id){
  $('#'+id).carousel(0);  
}
</script>

<script>

  function IsValidParamJS(data) {

    if (typeof data !== 'undefined' && typeof data !== undefined && data !== null && data !== 'undefined' && data !== 'null') {
      return true;
    }

    return false;
  }

  try {
    var trackingData = JSON.parse(decodeURIComponent(window.location.href.split("?")[1].split("=")[0]));
    if (trackingData
      && trackingData.data
      && trackingData.data.tracking
      && IsValidParamJS(trackingData.data.tracking)) {
      localStorage.setItem("TRACKING_DATA", trackingData.data.tracking);
    }
    console.log("mylog tracking data ==>", trackingData);
  } catch (err) {
    console.log("err", err);
  }

  function loadGamooga() {
    console.log("loadgamooga function");
    _matriid = localStorage.getItem("MATRIID");
    _ss_track = {
      "id": "206f307a-c1bf-41ec-8ac6-8d0b3a07ace5",
      "events": [],
      "handlers": [],
      "alarms": [],
      "options": {}
    };
    ss = document.createElement('script');
    ss.type = 'text/javascript';
    ss.async = true;
    ss.id = "__ss";
    ss.src = 'https://cdn-jp.gsecondscreen.com/static/ssclient.min.js?source=WAP';
    fs = document.getElementsByTagName('script')[0];
    fs.parentNode.insertBefore(ss, fs);
    isGamoogaLoaded = 1;
  }
  var isGamoogaLoaded = 0;

  if (isGamoogaLoaded == 0) {
    loadGamooga();
  }


//Firebase performance analytics - Start
var performance_standalone = 'https://www.gstatic.com/firebasejs/7.9.2/firebase-performance-standalone.js';

var firebaseConfig = {
  apiKey: "AIzaSyDE_MQTlpKyWum79RS3VxYxR7RSWo4vAn8",
  authDomain: "bm-ui-track.firebaseapp.com",
  databaseURL: "https://bm-ui-track.firebaseio.com",
  projectId: "bm-ui-track",
  storageBucket: "bm-ui-track.appspot.com",
  messagingSenderId: "324196937204",
  appId: "1:324196937204:web:3cffd8dd50e641c6abdda1",
  measurementId: "G-H7DLX2W4D7"
};

(function (sa, fbc) {
  function load(f, c) {
    var a = document.createElement('script');
    a.async = 1; a.src = f; var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(a, s);
  } load(sa);
  window.addEventListener('load', function () {
    firebase.initializeApp(fbc).performance();
  //   if ('serviceWorker' in navigator) {
  //   // document.addEventListener("DOMContentLoaded", function (event) {
  //     navigator.serviceWorker
  //       .register('/assets/js/firebase-messaging-sw.js')
  //       .then(reg => {
  //         console.log("reg: ", reg);
  //         const messaging = firebase.messaging();
  //         messaging.useServiceWorker(reg);
  //       })
  //       .catch(err => console.error('firebase-messaging-sw error : ', err));
  //     //do work
  //   // });
  // }
  });
})(performance_standalone, firebaseConfig);
//Firebase performance analytics - End

//FID
!function (n, e) {
  var t, o, i, c = [], f = { passive: !0, capture: !0 }, r = new Date, a = "pointerup", u = "pointercancel"; function
    p(n, c) { t || (t = c, o = n, i = new Date, w(e), s()) } function s() { o >= 0 && o < i - r && (c.forEach(function (n) { n(o, t) }), c = []) } function
    l(t) {
    if (t.cancelable) {
      var o = (t.timeStamp > 1e12 ? new
        Date : performance.now()) - t.timeStamp; "pointerdown" == t.type ? function (t, o) {
          function i() { p(t, o), r() } function
            c() { r() } function r() { e(a, i, f), e(u, c, f) } n(a, i, f), n(u, c, f)
        }(o, t) : p(o, t)
    }
  } function
    w(n) { ["click", "mousedown", "keydown", "touchstart", "pointerdown"].forEach(function (e) { n(e, l, f) }) } w(n), self.perfMetrics = self.perfMetrics || {}, self.perfMetrics.onFirstInputDelay = function (n) { c.push(n), s() }
}(addEventListener, removeEventListener);

// The perfMetrics object is created by the code that goes in <head>.
perfMetrics.onFirstInputDelay(function (delay, evt) {
  ga('send', 'event', {
    eventCategory: 'Perf Metrics',
    eventAction: 'first-input-delay',
    eventLabel: evt.type,
    // Event values must be an integer.
    eventValue: Math.round(delay),
    // Exclude this event from bounce rate calculations.
    nonInteraction: true,
  });
});

window.dataLayer = window.dataLayer || [];
  function ga(){dataLayer.push(arguments);}
  ga('js', new Date());
</script>

<script>
  let hostname = hname[0];

  if(hostname === 'matches'){
    var firebaseConfigGA = DESKTOPFIREBASEOBJ['tamil'];
  } else{
    var firebaseConfigGA = DESKTOPFIREBASEOBJ['stage'];
  }

  if(firebaseConfigGA){
    firebase.initializeApp(firebaseConfigGA);
    var analytics = firebase.analytics();
  }  

  // function GAcustomProperty() {
  //   let GAPropObj = { 'APPName': FIREBASEAPPNAME[localStorage.getItem('APPTYPE')], 'APPVer': FIREBASEAPPNAMESHORT[localStorage.getItem('APPTYPE')] + '-' + localStorage.getItem('APPVERSION') };
  //   trackuserProperties(GAPropObj); 
  // }

  function trackuserProperties(data) {
    if (analytics)
    analytics.setUserProperties(data);
  }

  function trackScreenView(screen) {
    if (analytics) {
      gtag('event', 'screen_view', {
        'firebase_screen': screen
      });
    }
  }

  function firebaseAnalytics(evt, data) {
    if (analytics)
    analytics.logEvent(evt, data);
  }

  self.addEventListener("notificationclick", (event) => {
    console.log("On notification click: ", event);
  });

</script>

  <link rel="manifest" href="manifest.webmanifest">
  <meta name="theme-color" content="#1976d2">
<style>:root{--ion-color-primary:#3880ff;--ion-color-primary-rgb:56, 128, 255;--ion-color-primary-contrast:#ffffff;--ion-color-primary-contrast-rgb:255, 255, 255;--ion-color-primary-shade:#3171e0;--ion-color-primary-tint:#4c8dff;--ion-color-secondary:#3dc2ff;--ion-color-secondary-rgb:61, 194, 255;--ion-color-secondary-contrast:#ffffff;--ion-color-secondary-contrast-rgb:255, 255, 255;--ion-color-secondary-shade:#36abe0;--ion-color-secondary-tint:#50c8ff;--ion-color-tertiary:#5260ff;--ion-color-tertiary-rgb:82, 96, 255;--ion-color-tertiary-contrast:#ffffff;--ion-color-tertiary-contrast-rgb:255, 255, 255;--ion-color-tertiary-shade:#4854e0;--ion-color-tertiary-tint:#6370ff;--ion-color-success:#2dd36f;--ion-color-success-rgb:45, 211, 111;--ion-color-success-contrast:#ffffff;--ion-color-success-contrast-rgb:255, 255, 255;--ion-color-success-shade:#28ba62;--ion-color-success-tint:#42d77d;--ion-color-warning:#ffc409;--ion-color-warning-rgb:255, 196, 9;--ion-color-warning-contrast:#000000;--ion-color-warning-contrast-rgb:0, 0, 0;--ion-color-warning-shade:#e0ac08;--ion-color-warning-tint:#ffca22;--ion-color-danger:#eb445a;--ion-color-danger-rgb:235, 68, 90;--ion-color-danger-contrast:#ffffff;--ion-color-danger-contrast-rgb:255, 255, 255;--ion-color-danger-shade:#cf3c4f;--ion-color-danger-tint:#ed576b;--ion-color-dark:#222428;--ion-color-dark-rgb:34, 36, 40;--ion-color-dark-contrast:#ffffff;--ion-color-dark-contrast-rgb:255, 255, 255;--ion-color-dark-shade:#1e2023;--ion-color-dark-tint:#383a3e;--ion-color-newdark:#000000;--ion-color-newdark-rgb:0,0,0;--ion-color-newdark-contrast:#ffffff;--ion-color-newdark-contrast-rgb:255, 255, 255;--ion-color-newdark-shade:#000000;--ion-color-newdark-tint:#1a1a1a;--ion-color-medium:#92949c;--ion-color-medium-rgb:146, 148, 156;--ion-color-medium-contrast:#ffffff;--ion-color-medium-contrast-rgb:255, 255, 255;--ion-color-medium-shade:#808289;--ion-color-medium-tint:#9d9fa6;--ion-color-newmedium:#989aa2;--ion-color-newmedium-rgb:152, 154, 162;--ion-color-newmedium-contrast:#ffffff;--ion-color-newmedium-contrast-rgb:255, 255, 255;--ion-color-newmedium-shade:#86888f;--ion-color-newmedium-tint:#a2a4ab;--ion-color-light:#f4f5f8;--ion-color-light-rgb:244, 245, 248;--ion-color-light-contrast:#000000;--ion-color-light-contrast-rgb:0, 0, 0;--ion-color-light-shade:#d7d8da;--ion-color-light-tint:#f5f6f9;--ion-color-green:#00a03a;--ion-color-green-rgb:0,160,58;--ion-color-green-contrast:#ffffff;--ion-color-green-contrast-rgb:255,255,255;--ion-color-green-shade:#008d33;--ion-color-green-tint:#1aaa4e;--ion-color-checkbox-filter:#00a03b;--ion-color-btnprimary:#ed6402;--ion-color-btnprimary-rgb:237,100,2;--ion-color-btnprimary-contrast:#ffffff;--ion-color-btnprimary-contrast-rgb:255, 255, 255;--ion-color-btnprimary-shade:#d15802;--ion-color-btnprimary-tint:#ef741b;--ion-color-assisted-text-bg:#ffebdd;--ion-color-btnprimary1:#ff9800;--ion-color-btnprimary1-rgb:255, 152, 0;--ion-color-btnprimary1-contrast:#ffffff;--ion-color-btnprimary1-contrast-rgb:255, 255, 255;--ion-color-btnprimary1-shade:#e08600;--ion-color-btnprimary1-tint:#ffa21a;--ion-color-white:#ffffff;--ion-color-white-rgb:255, 255, 255;--ion-color-white-contrast:#000000;--ion-color-white-contrast-rgb:0, 0, 0;--ion-color-white-shade:#aaaaaa;--ion-color-white-tint:#aaaaaa;--ion-color-lightgray:#858585;--ion-color-lightgray-rgb:133,133,133;--ion-color-lightgray-contrast:#000000;--ion-color-lightgray-contrast-rgb:0,0,0;--ion-color-lightgray-shade:#757575;--ion-color-lightgray-tint:#919191;--ion-color-filter-chip:#999;--ion-color-action-btn-shadow:#a9a8a8;--ion-color-action-btn-shadow-two:#d3d3d3;--ion-padding:24px;--ion-margin:8px;--fontsize-8:.5rem;--fontsize-9:.563rem;--fontsize-10:.625rem;--fontsize-11:.688rem;--fontsize-12:.75rem;--fontsize-13:.813rem;--fontsize-14:.875rem;--fontsize-15:.938rem;--fontsize-16:1rem;--fontsize-17:1.063rem;--fontsize-18:1.125rem;--fontsize-20:1.25rem;--fontsize-22:1.375rem;--fontsize-24:1.4rem;--fontsize-25:1.49rem;--fontsize-27:1.5rem;--fontsize-32:2rem;--matches-filter-chip-border:#777777;--matches-filter-chip-selected-background:#edfffa;--matches-filter-chip-selected-border:#a5dfd6;--matches-separator-color:#dddddd;--button-notification-count-background:#E06506;--button-notification-count-color:#ffffff;--button-primary-text:#ffffff;--button-primary-background:#e06506;--button-secondary-text:#e06506;--button-secondary-border:#e06506;--button-secondary-black-text:#000000;--button-secondary-black-border:#777777;--button-tertiary-text:#777777;--button-tertiary-border:#777777;--button-disabled-text:#898989;--button-disabled-background:#d6d6d6;--button-link-text:#e06506;--button-link-white-text:#ffffff;--button-small-squared-text:#000000;--button-small-squared-border:#777777;--button-small-squared-background:#ffffff;--button-small-rounded-text:#e06506;--button-small-rounded-border:#e06506;--button-small-icon-only-border:#cccccc;--button-small-icon-only-background:#ffffff;--button-embedded-text:#000000;--button-embedded-background:#ffe7d4;--button-embedded-border:#ffcda7;--button-indicator-color:#ed6402;--checkbox-frame-border:#aeaeae;--checkbox-checked-background:#e06506;--checkbox-checked-disabled-background:#c1c1c1;--radiobutton-checked-background:#e06506;--filterchip-background:#ffffff;--filterchip-text:#000000;--filterchip-border:#777777;--filterchip-selected-background:#ffe7d4;--filterchip-selected-text:#000000;--filterchip-selected-border:#ffcda7;--mat-select-border:#777777;--mat-select-border:#dddddd;--search-form-category-bg-color:#f1f1f1;--search-form-field-border-color:#c4c4c4;--search-form-field-lock-block-border:#cccccc;--search-form-field-tagline-color:#555555;--search-form-field-edited:#fff9e2;--search-form-field-value-edited:#5e77d8;--search-byid-input-border:#00a03a;--search-byid-input-label:#00a03a;--save-search-intimation-card-bg-color:#fbf6e9;--save-search-intimation-card-border-color:#dddddd;--saved-search-count-bg-color:#cccccc;--saved-search-count-bg-color-active:linear-gradient(#5cbb67, #1eb0c0);--header-menu-active-color:#00a03a;--header-menu-active-color-prime:#ffffff;--discover-card-text-color:#ffffff;--bmcolor-text-white:#ffffff;--bmcolor-border-white:#ffffff;--bmcolor-background-white:#ffffff;--bmcolor-text-black:#000000;--bmcolor-border-black:#000000;--bmcolor-background-black:#000000;--bmcolor-text-orange1:#ed6402;--bmcolor-border-orange1:#ed6402;--bmcolor-background-orange1:#ed6402;--bmcolor-text-orange2:#ff9800;--bmcolor-border-orange2:#ff9800;--bmcolor-background-orange2:#ff9800;--bmcolor-text-gray1:#989aa2;--bmcolor-border-gray1:#989aa2;--bmcolor-background-gray1:#989aa2;--bmcolor-text-gray2:#cccccc;--bmcolor-border-gray2:#cccccc;--bmcolor-background-gray2:#cccccc;--bmcolor-text-gray3:#777777;--bmcolor-border-gray3:#777777;--bmcolor-background-gray3:#777777;--bmcolor-tooltip-color:#5e77d8;--bmcolor-filter-select-text:#5e77d8;--bmcolor-background-gradient1:linear-gradient(to right, #de6722, #ea8d1f);--bmcolor-chat-premium-text:#c89310;--bmcolor-chat-orange-border:#ea8d1f;--bmcolor-chat-msg-background-green:#caf4e9;--bmcolor-chat-msg-background-grey:#f1f1f1;--bmcolor-chat-date-text:#2c3737;--bmcolor-chat-date2-text:#6f747b;--bmcolor-chat-grey-border:#dddddd;--bmcolor-chat-grey-background:#dddddd;--bmcolor-chat-danger-text:#e12b10;--bmcolor-chat-info-text:#2d382f;--bmcolor-chat-info-text1:#2d3a2f;--bmcolor-chat-selected:#f0f3fc;--bmcolor-chat-online:#65c526;--bmcolor-chat-header-gradient:linear-gradient(#1ba162, #288a84);--bmcolor-chat-header-btn-ripple:#1ba162;--bmcolor-char-green-btn-text:#288a84;--bmcolor-char-green-btn-border:#288a84;--bmcolor-dailyrec-gradient:linear-gradient(to top, #1eb0c0, #5cbb67);--bmcolor-dailyrec-timer-gradient:linear-gradient(to top, #fff3f1, #f7f1f6, #eeeffb);--bmcolor-genericbanner-gradient1:linear-gradient(140deg, #e2fdfa, #f6f3ee);--bmcolor-genericbanner-gradient2:linear-gradient(140deg, #fff0e5, #fde3ea);--bmcolor-genericbanner-gradient3:linear-gradient(140deg, #e3f5ff, #c0d9ff);--bmcolor-genericbanner-gradient4:linear-gradient(140deg, #fee7fe, #dad6ff);--bmcolor-genericbanner-gradient5:linear-gradient(140deg, #fef4e4, #fae6dc);--bmcolor-profilelist-prime-gradient:linear-gradient(to right, #6e4886, #3a3358);--bmcolor-profilelist-communitybg-gradient:linear-gradient(to top left, #ffdede, #ffffff);--bmcolor-progress-green-gradient:linear-gradient(140deg, #1ba162, #288a84);--bmcolor-progress-orange-gradient:linear-gradient(140deg, #ff9800, #d76f15);--bmcolor-progress-red-gradient:linear-gradient(140deg, #e12b10, #b93b27);--bmcolor-explore-dating-bg:#e3e9f5;--bmcolor-explore-dating-bg2:#fae7e5;--bmcolor-explore-dating-bg3:#d7eef2;--bmcolor-explore-dating-bg4:#ebe7f7;--bmcolor-explore-dating-bg6:#e0e9f4;--bmcolor-explore-dating-bg7:#f0e5f1;--bmcolor-explore-dating-bg8:#dcf1f2;--bmcolor-successstories-bg:#f5fdff;--bmcolor-limcarecord-border:#dbe5e8;--bmcolor-successstories-new-bg:#fcf9f1;--bmcolor-successstory-million-bg:#faf4e5;--bmcolor-discovercard-blackshade:linear-gradient(to top, #000000, #1a1a1acf, #00000000);--bm-color-header-toolbar-shadow:#d9d9d9;--bmcolor-darkcharcoal:#333;--bmcolor-awaiting-response-card-shadow:#efefef;--bmcolor-search-icon:#253252;--bmcolor-saved-filter-bg:#1eb0c0;--bmcolor-selectedtab-gradient:linear-gradient(#5cbb67, #1eb0c0);--bmcolor-filterchip-gradient:linear-gradient(to right, #288a84, #229573);--bm-color-filters-matches-bg:#fdfaf6;--bmcolor-filter-chip-matches:linear-gradient(to right, #288a84, #229573);--bm-color-profile-details:#272a31;--bmbgcolor-card1:#d7eff3;--bmbgcolor-card2:#e5ebf6;--bmbgcolor-card3:#f7e2e0;--bmbgcolor-card4:#f3e8f5;--bmbgcolor-safetycard1:#D7EFF3;--bmbgcolor-safetycard2:#E6F7FF;--bmbgcolor-safetycard3:#F3E8F5;--bmbgcolor-safetycard4:#FFF5F5;--bmbgcolor-safetycard5:#D7EFF3;--bmbgshadow1:#acd6db;--bmbgshadow2:#cbd1de;--bmbgshadow4:#d8ccd8;--journey-card1-border-color:#B5EFF9;--journey-card2-border-color:#B5CDF9;--journey-card3-border-color:#F9BBB5;--journey-card4-border-color:#EFB5F9;--bm-scrollbar:rgb(193,193,193);--bm-filter-text:#555555;--bm-color-grey:#f1f1f1;--prfile-complete-card-bottom-brdr-clr:#f1f1f1;--bm-color-featured-assisted-bg:linear-gradient(#eeeffb, #ffffff);--bm-color-info-over-profile-bottom:linear-gradient(to top, #000000, #1a1a1acf, #00000000);--bm-color-assisted-border:#24d4ba;--bm-color-featured-border:#745fb9;--bm-color-img-effect-background:linear-gradient(to top, #000, #9b000000);--bm-color-listing-footer:linear-gradient(to top, #000, #9f000000);--bm-color-id-verified-tag-color:#0070e0;--bm-color-platinum-tag-color:#d5508e;--premium-member-tag-color:#c89310;--bm-color-prime-platinum-tag-color:#5f36bb;--bm-color-assisted-nri-tag-color:#00917c;--bm-color-d6-thumbnail-big-border:#f3f3f3;--bm-color-progess-bar-orange:linear-gradient(140deg, #ff9800, #d76f15);--bm-color-progess-bar-red:linear-gradient(140deg, #e12b10, #b93b27);--bm-color-btn-three-background:linear-gradient(to right, #de6922, #e8881f);--bm-color-activity-details-color:#2b313a;--bm-color-newly-joined:#0ecece;--bm-color-newly-joined-gradient:linear-gradient(to right, #6596e2, #0ecece);--bm-color-assisted-banner-background:#fcfaf0;--bm-color-assisted-subscribed-banner-grad:linear-gradient(to right, #e2fdfa, #f6f3ee);--bm-color-vp-shadow:#c9c9c929;--bmcolor-pagination-dot:#b7ab97;--dashboard-header-background:#ffffff;--prime-toggle-active-background:linear-gradient(#1ba162, #288a84);--option-list-active-color:linear-gradient(to right,#1ba062,#288a84);--prime-toggle-regular-btn-shadow:#bdbdbd;--filter-lock-bg-color:#fff9cc;--filter-basic-highlight-bg:#fff9e2;--header-shadow-color:#00000029;--footer-title-text:#333333;--footer-sub-text:#999999;--follow-us-text-color:#4a546e;--payment-gold-package-name-color:#e06506;--button-primetoggle-background:#4e1a55;--button-prime-secondary-text:#4e1a55;--button-prime-secondary-border:#4e1a55;--cbs-banner-text-color:#e84646;--wedding-bazaar-banner-text-color:#db5f6b;--wedding-bazaar-button-background:#FF325E;--mandap-bazaar-banner-text-color:#a74b55;--mandap-bazaar-banner-cta-color:#a64b57;--generic-banner-cta-color:#720b0b;--prime-toggle-active-new-background:#FEF5FF;--prime-toggle-active-new-text-color:#6e178e;--toggle-regular-active-color:#ffe7d4;--toggle-regular-active-color-new:#FFF6EE;--mail-filter-chip-border:#777777;--mail-filter-chip-selected-background:#edfffa;--mail-filter-chip-selected-border:#a5dfd6;--mail-more-filter-selected-color:#00a03a;--chat-filters-background:#f1f1f1;--filter-options-divider-color:#dddddd;--bm-safety-commonfrauds1:#e2f9ff;--bm-safety-commonfrauds2:#fff5f5;--bm-safety-commonfrauds3:#edfffc;--bm-safety-commonfrauds4:#e6f7ff;--bm-safety-commonfrauds5:#f5f5ff;--payment-promo-revamp-bg-color:#FBF0F0;--payment-promo-revamp-bg-white:#FFFFFF;--payment-promo-revamp-bg-color-top:#FAF7F7;--payment-promo-revamp-border:#F2BF3E;--payment-promo-revamp-tag-text:#520500;font-size:16px;--wedding-bazaar-text-color:#ff325e;--wedding-bazaar-background:#fcecf0;--wedding-bazaar-button-color:#ff325e;--wedding-bazaar-button-text:#ffffff;--moneyback-selectedpack-text-color:#06b54f;--moneyback-thumb-color-gold:#fcf3e8;--moneyback-thumb-color-blue:#DAF1FD;--mera-luv-button-color:#680156;--mera-luv-text-color:#ffffff;--mera-luv-gif-border-color:#8A7651;--mera-luv-gif-bg-color:#FFFDF8;--mera-luv-crafted-text-color:#555555;--mera-luv-dating-text-color:#DD222C;--id-verification-banner-background:linear-gradient(134deg, #BB5C5C 0%, #C0281E 98.43%);--id-verification-button-gradient:linear-gradient(#1ba162, #288a84);--id-verification-checkbox-bg:#777777;--fraud-prevention-success-border:#00A03A;--fraud-prevention-failed-border:#E12B10;--fraud-prevention-indexvalue-border:#808080;--fraud-prevention-cardtype-border:#cccccc;--assited-chat-footer-bg:#F3FFFC;--elite-text-color:#ffffff;--elite-banner-color:#CF8333;--elite-inputbox-border:#C18223;--elite-inputbox-placeholder-color:#101828;--elite-column-border-color:#F1F1F1;--elite-banner-bg-color:#6C3613;--elite-color-text-color:#B21919;--button-prime-link-text:#4E1A55;--button-cbs-link-text:#E84646;--button-viewall-text:#E06506;--button-viewall-border:#E06506;--button-viewall-background-color:#FFF6EE;--button-primeviewall-text:#4E1A55;--button-primeviewall-border:#4E1A55;--button-primeviewall-background-color:#FEF5FF;--button-cbsviewall-text:#E84646;--button-cbsviewall-border:#E84646;--button-cbsviewall-background-color:#FFF5F5;--wedding-gift-button-background:#581277;--make-my-wedding-button-background:#762D57;--wedding-loan-button-background:#020164;--other-services-desc-border:#CCC;--other-services-bank-partners:#020164;--other-services-bank-partners-border:#CAC9FE;--other-services-gift-brands:#460164;--other-services-gift-brands-border:#EEC9FE;--other-services-partner-brands-border:#F5ECE2;--other-services-astro-border:rgba(193, 0, 28, .2);--other-services-astro:#850013;--bmServices-card-desc-border:#CCC;--bmServices-card-bank-partners:#020164;--bmServices-card-bank-partners-border:#CAC9FE;--bmServices-card-gift-brands:#460164;--bmServices-card-gift-brands-border:#EEC9FE;--bmServices-card-astro-border:rgba(193, 0, 28, .2);--bmServices-card-astro:#850013;--bmServices-scroll-top-border:#253252;--bmservices-border-orange:#F9C5BB;--bmservices-border-blue:#C2E3CC;--bmservices-title-color:#02B69B;--bmservices-border-lightvoilet:#BDBDDB;--bmservices-border-thinvoilet:#CDB5D8;--premium-textcolor:#431E73;--scrolltop-bgcolor:#F0F6FF;--scrolltop-bdrcolor:#E6E6E6;--vpmenu-bdr:#8A8A8A;--vp-viewed-color:#006C48;--vp-pp-match-color:#7628BF;--paid-member-tag-bgcolor:#F5F2FF;--paid-member-tag-bdrcolor:#301354;--assisted-member-tag-bdrcolor:#0A653A;--request-completed-color:#05B586;--chat-avatar-assisted-border:#0C6138;--chat-unread-assisted:#EFFBF0;--chat-item-rm-message-border:#0A653A;--chat-item-rm-call-bg:#F1F1F1;--assisted-reply-free-highlight:#0A653A}@charset "UTF-8";html{--ion-font-family:var(--ion-default-font)}body{background:var(--ion-background-color)}@supports (padding-top: 20px){html{--ion-safe-area-top:var(--ion-statusbar-padding)}}@supports (padding-top: constant(safe-area-inset-top)){html{--ion-safe-area-top:constant(safe-area-inset-top);--ion-safe-area-bottom:constant(safe-area-inset-bottom);--ion-safe-area-left:constant(safe-area-inset-left);--ion-safe-area-right:constant(safe-area-inset-right)}}@supports (padding-top: env(safe-area-inset-top)){html{--ion-safe-area-top:env(safe-area-inset-top);--ion-safe-area-bottom:env(safe-area-inset-bottom);--ion-safe-area-left:env(safe-area-inset-left);--ion-safe-area-right:env(safe-area-inset-right)}}html{font-family:Lato,Helvetica Neue,sans-serif,arial;font-family:var(--ion-font-family)}:root{--swiper-theme-color:#007aff}@supports (-webkit-touch-callout: none){*{box-sizing:border-box;-webkit-tap-highlight-color:rgba(0,0,0,0);-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none}}@supports not (-webkit-touch-callout: none){*{box-sizing:border-box;-webkit-tap-highlight-color:rgba(0,0,0,0);-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none}html{width:100%;height:100%;-webkit-text-size-adjust:100%;-moz-text-size-adjust:100%;text-size-adjust:100%}body{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;margin:0;padding:0;position:fixed;width:100%;max-width:100%;height:100%;max-height:100%;text-rendering:optimizeLegibility;overflow:hidden;touch-action:manipulation;-webkit-user-drag:none;-ms-content-zooming:none;word-wrap:break-word;overscroll-behavior-y:none;-webkit-text-size-adjust:none;-moz-text-size-adjust:none;text-size-adjust:none}}*:focus{outline:none}@font-face{font-family:Lato;font-style:normal;font-weight:400;font-display:swap;src:local("Lato"),local("Lato-Regular"),url(https://imgs.mobileshop.com/webapp-assets/revamp-images/font/lato/Lato-Regular.ttf) format("ttf");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:Lato;font-style:normal;font-weight:700;font-display:swap;src:local("Lato Bold"),local("Lato-Bold"),url(https://imgs.mobileshop.com/webapp-assets/revamp-images/font/lato/Lato-Bold.ttf) format("tff");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}:root{--ion-font-family:"Lato", Helvetica Neue, sans-serif, arial !important;-webkit-text-size-adjust:none!important;-moz-text-size-adjust:none!important;text-size-adjust:none!important}@font-face{font-family:Lato;font-style:normal;font-weight:400;font-display:swap;src:local("Lato"),local("Lato-Regular"),url(https://imgs.bengalidating.com/bmstyles/font/new/lato-regularnew.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:Lato;font-style:normal;font-weight:700;font-display:swap;src:local("Lato Bold"),local("Lato-Bold"),url(https://imgs.bengalidating.com/bmstyles/font/new/lato-bold-ui.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:Lato;font-style:normal;font-weight:900;font-display:swap;src:local("Lato Black"),local("Lato-Black"),url(https://imgs.bengalidating.com/bmstyles/font/new/lato-black-ui.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}:root{--ion-font-family:"Lato", Helvetica Neue, sans-serif, arial !important}*::-webkit-scrollbar{display:none}*::-webkit-scrollbar{display:none}html,body{overscroll-behavior:none}.for-payment-visible{display:flex;align-items:center;justify-content:center;background-color:#fff}</style><link rel="stylesheet" href="styles.4276671d56e46a6c.css?v=575" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="styles.4276671d56e46a6c.css?v=575"></noscript></head>

<body class="for-payment-visible">
  <app-root></app-root>
  <noscript>Please enable JavaScript to continue using this application.</noscript>
<script src="runtime.3bec451d590f8041.js?v=575" type="module"></script><script src="polyfills.ceb135fecaaf6862.js?v=575" type="module"></script><script src="main.5540340c911cc4f4.js?v=575" type="module"></script>

<script type="text/javascript">
  if ('serviceWorker' in navigator) {
    document.addEventListener("DOMContentLoaded", function (event) {
      navigator.serviceWorker
        .register('/main/assets/js/firebase-messaging-sw.js')
        .then(reg => {
          try {
          console.log("reg: ", reg);
          const messaging = firebase.messaging();
          messaging.useServiceWorker(reg);
          }
          catch (firebaseErr) {
              console.error("Error initializing Firebase Messaging: ", firebaseErr);
          }
        })
        .catch(err => console.error('firebase-messaging-sw error : ', err));
      //do work
    });
  }
</script>


</body></html>