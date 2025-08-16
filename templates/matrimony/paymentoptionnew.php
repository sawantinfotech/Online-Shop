
<!DOCTYPE html>
<html lang="en">

<head>
  <meta name="keywords" content="" />
  <meta name="description" content="" />
  <title>MbobileShop.com</title>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://mbobileshop.com/styles/swiper-bundle.min.css">
  <style>
    .font-weight-bold {
      font-weight: bold;
    }

    .font-weight-boldnew {
      font-weight: 400;
    }

    @font-face {
      font-family: 'Lato';
      font-style: normal;
      font-weight: 400;
      font-display: swap;
      src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v16/S6uyw4BMUTPHjx4wXg.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    @font-face {
      font-family: 'Lato';
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v16/S6u9w4BMUTPHh6UVSwiPGQ.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    @font-face {
      font-family: 'Lato';
      font-style: normal;
      font-weight: 900;
      font-display: swap;
      src: local('Lato Black'), local('Lato-Black'), url(https://fonts.gstatic.com/s/lato/v16/S6u9w4BMUTPHh50XSwiPGQ.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    body {
      font-family: Lato, sans-serif;
      margin: 0px;
      auto;
    }

    #bmfont {
      font-family: Lato, sans-serif;
    }

    .chip-pad {
      padding-top: 5px;
      padding-bottom: 10px;
    }

    .update-chip-active {
      border-radius: 30px;
      background-image: linear-gradient(to bottom, #1ba162, #288a84);
      float: left;
    }

    .update-chip-inactive {
      border-radius: 40px;
      border: solid 1px #777777;
      float: left;
    }

    .update-chip-inner {
      background-color: #ecf7ff;
      border: none;
      color: #000;
    }

    .update-chip-label {
      text-align: center;
      padding: 18px 25px;
      line-height: 0px;
      color: #FFF;
    }

    .update-chip-label-1 {
      padding: 22px 12px;
      line-height: 0px;
      color: #000;
    }

    .payment-info-box {
      float: left;
      margin-left: 30px;
      margin-top: 20px;
      width: 248px !important;
      height: 463px;
      border-radius: 8px;
      box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.15);
      background-color: #ffffff;
      margin-bottom: 20px;
      border: 1px solid #fff;
    }

    .payment-cards {
      margin-top: 35px;
    }

    .pos-relative {
      position: relative;
    }

    .hpmainwraper {
      width: 100%;
      margin: 0px auto;
    }

    .clearfix::after {
      content: "";
      clear: both;
      display: table;
    }

    .inner-wrapper {
      width: 1200px;
      margin: 0px auto;
    }

    .logobox {
      float: left;
      padding: 14px 0px;
    }

    .fleft {
      float: left;
    }

    .fright {
      float: right;
    }

    .paytopqueries {
      margin-top: 30px;
      float: right;
      letter-spacing: 0.36px;
      font-size: 12px;
      color: #000;
      text-align: center;
    }

    .fntsmall {
      font-size: 12px;
    }

    .fntmedium {
      font-size: 14px;
    }

    .fntlarge {
      font-size: 20px;
    }

    .topsep {
      background: #00a03a;
      height: 2px;
      width: 100%;
    }

    .paytoppromotxt {
      letter-spacing: 0.66px;
      line-height: 22px;
      font-weight: 700;
      padding-top: 22px;
      color: #97009d;
      text-align: center;
      margin-bottom: -5px;
    }

    .paytoppromotxtbig {
      font-size: 22px;
      font-weight: 900;
    }

    .payselmempack {
      letter-spacing: 0.66px;
      line-height: 22px;
      font-weight: 700;
      color: #000;
      text-align: center;
      padding-bottom: 20px;
      font-size: 22px;
    }

    .package-selected {
      border: 1px solid #1ba162;
      cursor: pointer;
    }

    .payment-info-box:first-child {
      margin-left: 3px;
    }

    .payment-info-box:last-child {
      margin-right: 3px;
    }

    .payment-list-items {
      border-bottom: 1px solid #e0e0e0;
      margin-bottom: 12px;
      float: left;
      min-height: 250px;
    }

    .payment-list-items ul li {
      text-align: left;
    }

    .payment-tag-img {
      position: absolute;
      top: -10px;
      float: left;
      margin-left: 0%;
    }

    .payment-success-story {
      margin: 0 auto;
      width: 840px;
      float: none;
      overflow: hidden;
    }

    .payment-ss-content {
      float: left;
      width: 250px !important;
      margin-right: 30px;
    }

    .payment-ss-img {
      float: left;
      width: 100%;
    }

    .payment-ss-img img {
      border-top-left-radius: 10px;
      border-top-right-radius: 10px;
    }

    .payment-ss-text {
      float: left;
      padding: 14px 0px 12px 10px;
      background-color: #fff;
      width: 240px;
      margin-top: -3px;
      border-bottom-left-radius: 10px;
      border-bottom-right-radius: 10px;
    }

    .payment-ss-text1 {
      float: left;
      display: block;
      font-size: 14px;
      font-weight: bold;
      width: 100%;
    }

    .payment-ss-text2 {
      float: left;
      display: block;
      font-size: 12px;
      width: 100%;
    }

    .payment-success-button {
      width: 283px;
      margin: 33px auto;
      float: none;
    }

    .payment-ss-button {
      background-color: #ff9800;
      padding: 8px 16px;
      border-radius: 5px;
      font-size: 14px;
      color: #fff;
      text-decoration: none;
      text-transform: uppercase;
      font-weight: bold;
      text-align: center;
    }

    .btn-pay-now {
      margin-top: 0px;
    }

    .btn-pay-now-discount {
      margin-top: 25px;
    }

    .width-100 {
      width: 100%;
    }

    .inner-tabs-width {
      float: none;
      width: 1100px;
      margin: 0px auto;
    }

    .inner-tabs-border {
      float: left;
      width: 18%;
      border: 1px solid #ccc;
      margin-top: 19px;
    }

    .tabs-margin-bottom {
      margin-bottom: 4px
    }

    .mb-20 {
      margin-bottom: 20px;
    }

    .tabs-chip-width {
      float: left;
      width: 60%;
    }
    .till-marrychip {    
      padding:1px 10px !important;
      line-height: 17px !important;
      font-size: 14px !important;
      font-weight: 600;
      text-align: center !important;
    }

    .pay-icon-pos {
      background-position: 0px 8px !important;
    }

    # Swipe Left and Right CSS # .package-swiper-container {
      width: 1100px;
      height: 100%;
    }

    .package-swiper-slide {
      text-align: center;
      font-size: 18px;
      background: #fff;
      cursor: pointer;
      /* Center slide text vertically */
      display: -webkit-box;
      display: -ms-flexbox;
      display: -webkit-flex;
      display: flex;
      -webkit-box-pack: center;
      -ms-flex-pack: center;
      -webkit-justify-content: center;
      justify-content: center;
      -webkit-box-align: center;
      -ms-flex-align: center;
      margin-bottom: 40px;
    }

    .left {
      float: left;
      clear: left;
    }

    .right {
      float: right;
      clear: right
    }

    .paynow-button {
      -webkit-border-radius: 2px !important;
      -moz-border-radius: 2px !important;
      border-radius: 8px !important;
      background-color: #ff9800;
      color: #fff;
      cursor: pointer;
      padding: 10px 63px;
      letter-spacing: 0.66px;
      line-height: 22px;
      font-weight: 500;
      text-align: center;
      display: inline-block;
      text-decoration: none;
      font-size: 14px;
      text-transform: uppercase;
      border-radius: 10px;
    }
    .knowmore-button{
      color: #E06506;
      cursor: pointer;
      text-align: center;
      display: inline-block;
      text-decoration: none;
      font-size: 14px;
    }

    /* Style the tab */
    .tab {
      border-right: 1px solid #ccc;
      background-color: #FFF;
      width: 190px;
    }

    /* Style the buttons inside the tab */
    .tab div {
      display: block;
      outline: none;
      text-align: left;
      cursor: pointer;
      transition: 0.3s;
      font-size: 16px;
    }

    /* Change background color of buttons on hover 
.tab div:hover {
background-color: #ddd;
}
*/
    /* Create an active/current "tab button" class */
    .tab div.active {
      background-image: linear-gradient(107deg, #1ba162 3%, #288a84 96%);
    }

    /* Style the tab content */
    .tabcontent {
      float: left;
      border-left: none;
    }

    .d-none {
      display: none;
    }

    .inactivelabel {
      text-align: center;
      padding: 18px 25px;
      0px;
      line-height: 0px;
    }

    .tooltip {
      display: inline-block;
      position: absolute;
      width: 22px;
      height: 22px;
      cursor: pointer;
      margin-left: -67px;
      margin-top: 44px;
    }

    .tooltip .tooltiptext {
      visibility: hidden;
      background-color: black;
      color: #fff;
      border-radius: 6px;
      position: absolute;
      z-index: 1;
      top: -29px;
      left: 30px;
      width: 300px;
      padding: 10px 20px;
      text-align: left;
    }

    .tooltip .tooltiptext::after {
      content: "";
      position: absolute;
      top: 50%;
      right: 100%;
      margin-top: -5px;
      border-width: 5px;
      border-style: solid;
      border-color: transparent black transparent transparent;
    }

    .tooltip:hover .tooltiptext {
      visibility: visible;
    }

    .btn-large {
      font-size: calc(1em + .25vw);
      padding: 12px 26px;
    }

    .btn-large {
      display: inline-block;
      border-radius: 11px;
      padding: .5em 1em;
      text-align: center;
      color: #fff;
      border: none;
      font-weight: 700;
      background-color: #ff9800;
      font-size: .9em;
      cursor: pointer;
      outline: 0;
      font-family: Calibri Bold, AvenirNext, Avenir, -apple-system, BlinkMacSystemFont, Lato Slab, Droid Serif, Segoe UI, Oxygen-Sans, Ubuntu, Cantarell, Georgia, serif;
    }

    .continue_btn {
      width: 316px;
      height: 40px;
      border-radius: 8px;
      background: #ff9800;
      color: #FFF;
      font: 100 14px/40px 'Lato', sans-serif;
      display: inline-block;
      text-align: center;
      cursor: pointer;
      position: relative;
      text-transform: uppercase;
      backface-visibility: hidden;
      box-sizing: border-box;
      letter-spacing: 0.42px;
      font-weight: bold;
      text-decoration: none;
    }

    .money-back-box {
      width: 100%;
      height: 564px;
      background-image: linear-gradient(113deg, #5cbb67, #1eb0c0);
      margin-top: 80px;
    }

    .payment-success-box {
      width: 100%;
      height: 500px;
      background: #f1f1f1;
      margin-top: 72px;
      padding-bottom: 40px;
    }

    .assisted-tab {
      border-radius: 8px;
      border: solid 1px #ff9800;
      cursor: pointer;
    }

    .payment-query-box {
      width: 914px;
      border-radius: 10px;
      background-color: #f1f1f1;
      margin-top: 40px;
      display: inline-block;
    }

    .assisted-list-items {
      margin-bottom: 20px;
      letter-spacing: 0.48px;
      margin-top: 35px;
    }

    .assisted-list-items ul li {
      margin-bottom: 20px;
      letter-spacing: 0.48px;
      background: url('https://imgs.MbobileShop.com/bmimgs/assisted/assisted-icon-tick.svg') no-repeat 0px 5px;
      padding-left: 30px;
      list-style: none;
    }

    .tab_underline:after {
      border-radius: 10px;
      height: 4px;
      position: absolute;
      top: 161px;
      content: "";
      background-color: #288a84;
      width: 140px;
      margin-left: -140px;
    }

    .package-prime {
      position: relative;
      top: -2px;
    }

    .pay-page {
      padding-top: 20px;
      width: 311px;
    }

    /* START MATRIMONY-319 */
    .package-prime-banner {
      display: block;
      margin-left: auto;
      margin-right: auto;
      margin-top: 25px;
      margin-bottom: 25px;
    }

    .prime_eligible_terms_and_conditions {
      width: 50%;
      margin-left: auto;
      margin-right: auto;
      margin-top: 40px;
      font-size: 12px;
      text-align: center;
    }

    .assprime_eligible_terms_and_conditions {
      width: 50%;
      margin-left: auto;
      margin-right: auto;
      margin-top: 14px;
      font-size: 12px;
      text-align: center;
    }

    .regular_eligible_terms_and_conditions {
      width: 50%;
      margin-left: auto;
      margin-right: auto;
      margin-top: 40px;
      font-size: 12px;
      text-align: center;
    }

    .tooltip-addon .tooltiptext-addon-2 {
      background-color: #5e77d8;
      color: #fff;
      border-radius: 6px;
      position: absolute;
      z-index: 2;
      top: 76px;
      left: 409px;
      width: 300px;
      padding: 38px 28px 10px;
      font-size: 14px;
      line-height: 20px;
      letter-spacing: 0.48px;
    }

    .tooltip-addon .tooltiptext-addon-2::after {
      content: url(https://mbobileshop.com/images/payment-revamp/pay-tooltip-arrow.png);
      position: absolute;
      top: -17%;
      right: 100%;
      margin-top: -5px;
      left: 182px;
      transform: rotate(87deg);
    }

    /* END MATRIMONY-319 */
    /* BMPAY-1032 Start */
    .swiper-button-next,
    .swiper-button-prev {
      margin-top: 20% !important;
      top: auto;
    }

    .assisted-supreme-scroll {
      height: 176px;
      min-height: 246px;
      overflow-y: scroll;
    }

    .assisted-supreme-scroll::-webkit-scrollbar {
      height: 5px;
      width: 5px;
      background-color: #fff;
    }

    .assisted-supreme-scroll::-webkit-scrollbar-thumb {
      background-color: #cccccc;
      height: 134px;
    }

    .assisted-supreme-scroll::-webkit-scrollbar-track {
      -webkit-box-shadow: inset 0 0 6px #fff;
      background-color: #fff;
    }

    /* BMPAY-1032 End */
    /* MATRIMONY-1165 Start - Simplified Payment Page  for desktop - Non EPR + EPR */
    .sunday-offer-list {
      font-size: 15px;
      line-height: 15px;
      letter-spacing: 0.36px;
      font-family: Lato;
      padding-top: 13px;
      padding-bottom: 5px;
      display: flex;
    }

    .sunday-offer-list ul {
      list-style-type: none;
      margin: 0 auto 14px;
    }

    .sunday-offer-list ul li {
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/tick-orange-simplify.svg) no-repeat 0px 4px;
      margin-left: 0px;
      padding-bottom: 14px;
      line-height: 18px;
      padding-left: 26px;
      /* list-style-image: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/tick-orange-simplify.svg); */
    }

    .sunday-offer-list ul li span.cross-tick {
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/cross-grey-simplify.svg) no-repeat 0px 4px;
      text-decoration: line-through;
      color: #777777;
    }

    .sunday-offer-list ul li span {
      margin-left: 0px;
    }

    .radio-box-border {
      display: inline-block;
      border: 1px solid #cccccc;
      padding: 15px 16px 10px;
      width: 128px;
      border-radius: 8px;
      text-align: center;
    }

    .radion-box-text1 {padding-top: 7px;margin-top: 11px;padding-bottom: 11px;border-bottom: 1px solid #f1f1f1;font-weight: 600;height: 38px;display: flex;justify-content: center;align-items: center;flex-wrap: wrap;border-top: 1px solid #f1f1f1;}

    .radion-box-text2 {
      color: #00a03a;
      font-size: 16px;
      font-weight: 900;
      letter-spacing: 0.42px;
      line-height: 17px;
      margin-bottom: 14px;
      margin-top: 14px;
      height: 17px;
    }

    .best-selling-text {
      background-color: #d73281;
      color: #fff;
      text-align: center;
      font-size: 14px;
      position: relative;
      top: 5px;
      border-top-left-radius: 10px;
      border-top-right-radius: 10px;
      padding: 8px;
      font-weight: bold;
      text-transform: uppercase;padding-bottom: 10px;
    }

    .best-selling-textimg:before {display: none;}
    .best-selling-textimg:after {display: none;}

    .active-radio-box {
      border: 2px solid #ff9800;
      position: relative;
      top: -1px;
      background: #fff5ef;
    }

    .container-radio {
      display: block;
      position: relative;
      padding-left: 0px;
      margin-bottom: 12px;
      cursor: pointer;
      font-size: 16px;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      font-weight: 900;
    }

    /* Hide the browser's default radio button */
    .container-radio input {
      /* position: absolute; */
      opacity: 0;
      cursor: pointer;
    }

    /* Create a custom radio button */
    .checkmark {
      position: absolute;
      top: 2px;
      height: 20px;
      width: 20px;
      background-color: #fff;
      border-radius: 50%;
      border: 1px solid #cccccc;
      margin-top: 10px;
      margin-left: 43%;
    }

    /* On mouse-over, add a grey background color */
    .container-radio:hover input~.checkmark {
      background-color: #ccc;
    }

    /* When the radio button is checked, add a blue background */
    .container-radio input:checked~.checkmark {
      background-color: #fff;
      border: 1px solid #e06b22;
    }

    /* Create the indicator (the dot/circle - hidden when not checked) */
    .checkmark:after {
      content: "";
      position: absolute;
      display: none;
    }

    /* Show the indicator (dot/circle) when checked */
    .container-radio input:checked~.checkmark:after {
      display: block;
    }

    /* Style the indicator (dot/circle) */
    .container-radio .checkmark:after {
      top: 3px;
      left: 3px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #e06b22;
    }

    .sunday-offer-list ul li span .benefits-bold {
      margin-left: 0px;
      display: inline-block;
      font-weight: bold;
    }

    .font-weight-bold {
      margin-left: 0px !important;
      font-weight: bold;
    }

    .radion-box-greytext {
      color: #777777;
      text-decoration: line-through;
      letter-spacing: 0.36px;
      font-weight: normal;
      display: block;
      margin-bottom: 7px;
      margin-top: 9px;
      height: 17px;
    }

    .radion-box-greyblack {
      font-size: 20px;
      letter-spacing: 0.42px;
      color: #000000;
      font-weight: 900;
      display: block;
      margin-top: 9px;
    }

    .radio-pack-text {
      margin-top: 28px;
      margin-left: -12px;
      margin-right: -12px
    }

    .simplify-offer {
      margin: 0px auto 10px;
      width: 100%;
      text-align: center;
    }

    .best-selling-text:after {
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/star-icon-simplify.svg);
      content: " ";
      width: 10px;
      height: 10px;
      margin-left: 4px;
      margin-top: 4px;
      position: absolute;
    }

    .best-selling-text:before {
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/star-icon-simplify.svg);
      content: " ";
      width: 10px;
      height: 10px;
      margin-left: -14px;
      margin-top: 4px;
      position: absolute;
    }

    .simplify-payment {
      margin: 0 auto 30px;
      display: block;
      color: #000000;
      font-size: 14px;
      line-height: 17px;
      font-family: Lato;
      letter-spacing: 0.42px;
    }

    .simplify-payment-title {
      font-size: 27px;
      line-height: 22px;
      letter-spacing: 0.54px;
      font-family: Lato;
      padding-top: 20px;
      padding-bottom: 25px;
      color: #000000;
      font-weight: 900;
      text-align: center;
      margin: 0 auto;
    }

    .simplify-payment-title-new {
      font-size: 22px;
      line-height: 22px;
      letter-spacing: 0.54px;
      font-family: Lato;
      padding-top: 20px;
      padding-bottom: 15px;
      color: #000000;
      font-weight: 900;
      text-align: center;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: left;
    }

    .simplify-payment-title-new img {
      margin-right: 10px;
    }

    .epr-payment-bg {
      background: #fef6db;
      padding: 20px 30px;
      text-align: center;
      margin-bottom: -7px;
    }

    .epr-payment-bg-img {
      margin: 0 auto;
      display: block;
      text-align: center;
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/epr-payment-bg.svg) no-repeat;
      width: 382px;
      height: 162px;
    }

    .epr-payment-offer {
      display: block;
      font-size: 22px;
      font-weight: 900;
      letter-spacing: 0.42px;
      margin-bottom: 10px;
      padding-top: 33px;
    }

    .epr-payment-offer-perc {
      display: block;
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 0.42px;
      margin-bottom: 10px;
      color: #662525;
      font-family: 'Lato';
      text-transform: uppercase;
      padding-top: 10px;
    }

    .epr-payment-offer-text {
      color: #ea1c1c;
      font-size: 18px;
      font-weight: 900;
      letter-spacing: 0.42px;
      margin-top: 10px;
    }

    .epr-simplify-offer {
      background: #fff5ef;
      margin: 0 auto 14px;
      text-align: center;
      width: 276px;
      padding: 18px;
      border-radius: 10px;
    }

    .epr-offer-pack {
      font-size: 16px;
      color: #e16f22;
      font-weight: 900;
      letter-spacing: 0.42px;
      margin-bottom: 2px;
      margin-top: 5px;
    }

    .epr-offer-amount {
      color: #444444;
      font-size: 14px;
      letter-spacing: 0.42px;
      text-decoration: line-through;
      opacity: 0.6;
    }

    .epr-offer-perc {
      color: #06b54f;
      font-size: 14px;
      font-weight: 900;
    }

    .epr-offer-pack-amount {
      font-size: 24px;
      font-weight: 900;
      letter-spacing: 0.42px;
    }

    .epr-offer-pack-month {
      font-size: 16px;
    }

    .sunday-offer-list ul li.cross-tick {
      background: url(https://imgs.MbobileShop.com/webapp-assets/images/payment/cross-grey-simplify.svg) no-repeat 0px 3px;
      text-decoration: line-through;
      color: #777777;
    }

    .mgb-img {
      text-align: center;
      padding-top: 8px;
    }

    .mgb-img img {
      cursor: pointer;
    }

    body.modal {
      overflow: hidden;
      position: fixed;
    }

    .modal {
      display: none;
      /* Hidden by default */
      position: fixed;
      /* Stay in place */
      z-index: 2;
      /* Sit on top */
      left: 0;
      top: 0;
      width: 100%;
      /* Full width */
      height: 100%;
      /* Full height */
      overflow: hidden;
      /* Enable scroll if needed */
      background-color: rgb(0 0 0 / 82%);
    }

    /* Modal Content/Box */
    .modal-content {
      background-color: #fefefe;
      margin: 29px auto;
      /* 15% from the top and centered */
      padding: 24px 24px 24px 20px;
      border: 1px solid #888;
      width: 360px;
      height: auto;
      /* Could be more or less, depending on screen size */
      font-size: 14px;
      line-height: 17px;
      font-family: Lato;
      letter-spacing: 0.42px;
    }

    /* The Close Button */
    .close {
      color: #253252;
      float: right;
      font-size: 32px;
      margin-right: -2px;
    }

    .close:hover,
    .close:focus {
      color: black;
      text-decoration: none;
      cursor: pointer;
    }

    .modal-header {
      font-family: Lato;
      font-size: 20px;
      font-weight: 700;
      line-height: 24px;
      text-align: left;
    }

    .modal-header p {
      font-family: Lato;
      font-size: 12px;
      font-weight: 400;
      line-height: 14.4px;
      text-align: left;
      margin: 8px 0px 11px 0px;
      /* padding-bottom: 8px; */
    }

    .pop-up-content p {
      font-family: Lato;
      font-size: 16px;
      font-weight: 400;
      line-height: 19.2px;
      text-align: left;
      margin-top: 0;
      margin-bottom: 10px;
      /* padding-bottom: 8px; */
    }

    .pop-up-list {
      padding-left: 19px;
    }

    .pop-up-list li {
      font-family: Lato;
      font-size: 14px;
      font-weight: 400;
      line-height: 17px;
      letter-spacing: 0.03em;
      text-align: left;
      padding-bottom: 8px;
    }

    .selected-pack {
      font-family: Lato;
      font-size: 16px;
      font-weight: 400;
      line-height: 19.2px;
      text-align: left;
      color: #06b54f;
    }

    .pack {
      font-family: Lato;
      font-size: 16px;
      font-weight: 700;
      line-height: 19.2px;
      text-align: left;
    }

    .period {
      font-family: Lato;
      font-size: 16px;
      font-weight: 400;
      line-height: 19.2px;
      text-align: left;
    }

    .btn-pay-now {
      font-family: Lato;
      font-size: 14px;
      font-weight: 700;
      line-height: 16.8px;
      letter-spacing: 0.03em;
      text-align: left;
      color: #FFFFFF;
      width: 100%;
      height: 40px;
      border-radius: 50px;
      /* background-color: #E06506; */
      text-align: center;
      border: none;
      cursor: pointer;
    }

    .btn-pay-now-mbg {
      font-family: Lato;
      font-size: 14px;
      font-weight: 700;
      line-height: 16.8px;
      letter-spacing: 0.03em;
      text-align: left;
      color: #FFFFFF;
      width: 100%;
      height: 40px;
      border-radius: 50px;
      background-color: #E06506 !important;
      text-align: center;
      border: none;
      cursor: pointer;
    }

    .terms {
      font-family: Lato;
      font-size: 12px;
      font-weight: 400;
      line-height: 14.4px;
      text-align: left;
      margin-bottom: 0;
    }

    .terms span a {
      color: #E06506;
      cursor: pointer;
      text-decoration: none;
    }

    .pop-up-img {
      padding: 0px 0px 8px;
      float: left;
      width: 100%;
    }

    .pop-up-img img {
      width: 100%
    }

    .modal-footer {
      border-top: 1px solid #CCCCCC;
    }
    /* Make the modal content scrollable */
        .modal-content-mac {
            max-height: 90vh; /* Set a maximum height for the modal content */
            overflow-y: auto; /* Enable vertical scrolling if content exceeds the max height */
        }

        /* Optionally, to prevent scrolling of the entire page when modal is open */
        body.modal-open {
            overflow: hidden; /* Prevent page from scrolling when modal is open */
    }

    /* MATRIMONY-1165 End  - Simplified Payment Page  for desktop - Non EPR + EPR */
    @media only screen and (min-width: 1368px) {
      .pay-page {
        width: 330px;
      }

      .modal-content-mac {
        margin: 30vh auto;
      }
    }

    /* BM-485 Css Start */
    .benefit-info-icon {
      position: relative;
      z-index: 999999;
    }

    .benefit-info-icon img {
      vertical-align: middle;
      margin-left: 1px;
    }

    .white-overlay-prime {
      position: fixed;
      height: 100%;
      background: white;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      opacity: 0.7;
      z-index: 9999;
    }

    .benefits-prime-tooltip {
      position: absolute;
      width: 304px;
      transform1: translateX(-37px);
      margin-top: 20px;
      background: #ffffff;
      border: 2px solid #00a03a;
      padding: 25px 10px 10px 10px;
      border-radius: 10px;
      line-height: normal;
      z-index: 999999;
      box-shadow: 3px 3px 8px 3px #f1f1f1;
      margin-left: -94px;
    }

    .benefits-prime-tooltip:before {
      content: " ";
      position: absolute;
      width: 0;
      height: 0;
      top: -1px;
      right: 197px;
      border-style: solid;
      border-width: 8px;
      border-color: transparent transparent #00a03a #00a03a;
      transform-origin: 0 0;
      -ms-transform-origin: 0 0;
      -webkit-transform-origin: 0 0;
      transform: rotate(155deg) skew(16deg, -24deg);
      -ms-transform: rotate(155deg) skew(16deg, -24deg);
      -webkit-transform: rotate(155deg) skew(16deg, -24deg);
      z-index: -1;
    }

    .benefits-prime-tooltip:after {
      content: " ";
      position: absolute;
      width: 0;
      height: 0;
      top: 2px;
      right: 197px;
      border-style: solid;
      border-width: 8px;
      border-color: transparent transparent #ffffff #ffffff;
      transform-origin: 0 0;
      -ms-transform-origin: 0 0;
      -webkit-transform-origin: 0 0;
      transform: rotate(155deg) skew(16deg, -24deg);
      -ms-transform: rotate(155deg) skew(16deg, -24deg);
      -webkit-transform: rotate(155deg) skew(16deg, -24deg);
    }

    .benefits-info-close {
      display: block;
      margin-top: -15px;
      margin-bottom: 0px;
      margin-right: 3px;
      float: right;
      cursor: pointer;
    }

    .benefits-info-title {
      font-weight: bold;
    }

    .benefits-info-list {
      padding-left: 2px;
    }

    .benefits-info-title,
    .benefits-info-list ul li {
      font-size: 14px;
      letter-spacing: 0.42px;
      font-family: 'Lato';
      background: none;
      padding-left: 0px;
    }

    .benefits-info-list ul {
      margin-top: 8px;
      padding-left: 30px;
      margin-bottom: 10px;
      list-style: disc;
    }

    .benefits-info-icon {
      position: relative;
      z-index: 1;
    }

    .benefits-info-icon-index {
      z-index: 9999;
    }

    .benefits-info-icon img {
      margin-top: -3px;
    }

    /* BM-485 Css End */
    /* welcome offer css start */
.main-box {
  max-width: 590px;
  margin: auto;
    padding: 10px 8px 10px 12px;
    background-color: #ffffff;
    background: url('https://imgs.MbobileShop.com/webapp-assets/revamp-images/desktop-welcome-offer-bg.png');
    background-size: cover;
}

    .content-col {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        position: relative;
    }

    .flat-offer {
        display: block;
        color: #FF5353;
        font-family: Lato;
        font-size: 32px;
        font-style: normal;
        font-weight: 800;
        line-height: normal;
    }

    .timer-section {
        display: flex;
        justify-content: flex-start;
        color: #FF2100;
  }

        .timer-subsection {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
    }

            .timer-box {
                border: 1px solid #D7D7D7;
                text-align: center;
                border-radius: 4px;
                align-items: center;
                justify-content: center;
                width: 22px;
                height: 25px;
                display: inline-flex;
            }

            .hour-sec-text {
                color: #444444;
                margin-top: 5px;
            }

    .column-cls {
        padding: 0 5px;
    }

    .offer-gif {
        width: 130px;
        height: 94px;
    }

    .col-content {
        min-width: fit-content;
        max-width: fit-content;
    }

    .d-flex {
        display: flex;
        align-items: center;
        justify-content: space-around;
    position: relative;
    }

    .bg-image {
        position: absolute;
        left: -6px;
        top: 6px;
    }
  .text-align-center{
    text-align: center;
  }
  .pb-5{
    padding-bottom: 5px;
  }
  .d-block{
    display: block;
  }
  .welcome-offer-text{
     font-size: 20px;
   font-weight: 700;
   font-family: 'Lato';
   line-height: normal;
  }
  .ml-2{
    margin-left:2px;
  }
  ul.pop-up-list.knw_list li {
    border-bottom: 2px dashed #ddd;
    padding-bottom: 15px;
    margin-bottom: 14px;
  }
  .disabled-link {
    pointer-events: none; /* Prevents clicking */
    opacity: 0.5; /* Makes it look disabled */
    cursor: not-allowed !important; /* Shows disabled cursor */
  }
  .popup-tum{
    padding: 7px 14px;
    margin-bottom: 20px;
    border-radius: 4px;
    border: 1px solid #F1F1F1;
    background: linear-gradient(90deg, rgba(255, 244, 225, 0.19) 0%, rgba(255, 255, 255, 0.19) 100%);
    font-size: 14px;
    font-weight: 700;
  }
/* welcome offer css end */
  </style>
</head>

<body onload="paymentTypeDet();">
  <div class="hpmainwraper pos-relative">
    <div class="inner-wrapper">
      <div class="logobox"><a href="https://profile.MbobileShop.com/login/myhome.php"><img src="https://imgs.MbobileShop.com/bmimgs/MbobileShop-logo.png" width="150" height="48" alt="MbobileShop.com" /></a></div>
      <span id="simplifychat"> </span>
    </div><br clear="all">
    <div class="topsep package-duration">
      <img src="https://imgs.MbobileShop.com/bmimgs/trans.gif" height="2" width="100%" alt="MbobileShop" />
    </div>
  </div>
  <!-- modal -->
  <div id="myModal" class="modal">
    <!-- Modal content -->
    <div class="modal-content modal-content-mac">
      <span class="close">&times;</span>
      <div class="pop-up-img">
        <img src="https://imgs.MbobileShop.com/webapp-assets/revamp-images/money-back/mb-thumb-without-info.svg" alt="Money Back Guarantee">
      </div>
      <div class="modal-header">
        Money back guarantee
        <p>Terms & Conditions*</p>
      </div>
      <div class="pop-up-content">
        <p>If the users meets the below conditions and do not find a match within 21 days, get a full refund ! No questions asked !</p>
        <ul class="pop-up-list">
          <li>User's must have added a minimum of 3 photos to his/her profile.</li>
          <li>User's profile  should be Govt ID verified.</li>
          <li>User's profile completion score must be at least 80%.</li>
          <li>User must  have messaged at least 15 mutually matching profiles in  first 21 days after membership purchase.</li>
          <li>User does not have a single reply on messages initiated by him/her.</li>
          <li>You should not have consumed any phone number  from his/her membership.</li>
          <li>21 Day Money Back guarantee is <b>only  applicable for self serve packs and  does not apply to any assisted package.</b></li>
        </ul>
      </div>
      <div class="modal-footer">
                <p class="terms"> <span> <a href="https://mbobileshop.com/terms.php?gaact=TERMS&gasrc=FOOTSUB&apptype=115?fromwebapps=webapps">Click here</a> </span> to view the Terms & Conditions </p>
      </div>
    </div>
  </div>
    <!-- modal -->
    <div id="myModal_smplytum" class="modal">
    <!-- Modal content -->
    <div class="modal-content modal-content-mac" style="border-radius: 25px;">
      <span class="close smply_knw_close" style="margin-right: 5px;">&times;</span>
      <div class="modal-header" style="font-size: 16px;letter-spacing: 0.42px;width: 90%;">What Makes Till U Marry the Best Choice</div>
      <div class="pop-up-content">
        <ul class="pop-up-list knw_list">
          <li><b>Search for your life partner without worrying about repeated payments</b></li>
          <li><b>Majority of paid users find their life partner within a year </b>– Till U Marry package gives you one year of paid membership benefits at a price lower than the 6M Prime Gold plan.</li>
          <li><b>Still searching after one year?</b> – Renew for another year at a guaranteed 75% discount, lower than the 3M Prime Gold price, if renewed within 2 weeks of package expiry.</li>
        </ul>
        <div class="popup-tum">Choose the only package you need to find your perfect match!</div>
      </div>
      <div class="modal-footer" style="border-top: 0px;margin: 0 auto;display: block;width: 100%;text-align: center;">
        <div id="knw_more_smply_pytm">
        </div>
      </div>
    </div>
  </div>
  <!-- modal -->
  <div id="myModal_tum" class="modal">
    <!-- Modal content -->
    <div class="modal-content modal-content-mac" style="border-radius: 25px;">
      <span class="close knw_close" style="margin-right: 5px;">&times;</span>
      <div class="modal-header" style="font-size: 16px;letter-spacing: 0.42px;width: 90%;">Why Choose the Till U Marry (TUM) Package?</div>
      <div class="pop-up-content">
        <ul class="pop-up-list knw_list">
          <li><b>Search for your life partner without worrying about repeated payments</b></li>
          <li><b>Majority of paid users find their life partner within a year </b>– Till U Marry package gives you one year of paid membership benefits at a price lower than the 6M Prime Gold plan.</li>
          <li><b>Still searching after one year?</b> – Renew for another year at a guaranteed 70% discount, lower than the 3M Prime Gold price, if renewed within 2 weeks of package expiry.</li>
        </ul>
        <div class="popup-tum">Choose the only package you need to find your perfect match!</div>
      </div>
      <div class="modal-footer" style="border-top: 0px;margin: 0 auto;display: block;width: 100%;text-align: center;">
        <div id="knw_more_pytm">
        </div>
      </div>
    </div>
  </div>
      <!-- welcome offer UI part end -->

  <!-- Simplified payment Start -->
  <div class="simplify-payment" id="simplifypayment" style="display:none;">
    <div>
       <!-- $GETDOMAININFO['domainnameshort'] == 'MbobileShop' --->
        <div class="mgb-img">
          <img src="https://imgs.MbobileShop.com/webapp-assets/revamp-images/money-back/mb-thumb-with-info.svg" height="94.73" width="422" alt="Money Back Guarantee" id="myBtn">
                  </div>
              <!-- <span style="position: absolute;right: 136px;cursor: pointer;margin-top: 14px;"><a href=""><img src="https://imgs.MbobileShop.com/bmimgs/desktop-intermediate/close-bg-filled-grey.svg" alt="Close button" style="vertical-align: middle;margin-left: 10px;"></a></span> -->
            <div class="simplify-payment-title">Pay now to contact matches</div>
      <div id="packbenefitdet">
      </div>
      <div class="simplify-offer">
        <div class="radio-box-border" id="goldpack1">
          <label class="container-radio">
            <input type="radio" id="goldpack" name="radio" onclick="paymentTypeDet(1);ajaxpayment('GOLD3MONTHS');">
            <input type="hidden" name="simplyfyurl" id="simplyfyurl" value="0">
            <div class="radio-pack-text">GOLD</div>
            <div class="radion-box-text1">3 Months</div>
                          <div class="radion-box-text2">
                <div>SAVE 58%</div>
              </div>
              <div>
                <span class="radion-box-greytext"><span>₹5,300</span></span>
                <span class="radion-box-greyblack">₹2,200</span></div>
                        <div class="checkmark"></div>
          </label>
        </div>
        <div style="display: inline-block;margin-left: 13px;">
          <div class="best-selling-text best-selling-textimg">Best Selling</div>
          <div class="radio-box-border" id="primegoldpack1">
            <label class="container-radio">
              <input type="radio" name="radio" id="primegoldpack" onclick="paymentTypeDet(327);ajaxpayment('PRIMEGOLD3MONTHS');">
              <div class="radio-pack-text">PRIME GOLD</div>
              <div class="radion-box-text1">3 Months</div>
                              <div class="radion-box-text2">
                  <div>SAVE 59%</div>
                </div>
                <div>
                  <span class="radion-box-greytext"><span>₹7,500</span></span>
                  <span class="radion-box-greyblack">₹3,100</span></div>
                            <div class="checkmark"></div>
            </label>
          </div>
        </div>
        <div style="display: inline-block;margin-left: 13px;">
        <div class="best-selling-text" style="display: none;">Best value</div>
        <div class="radio-box-border" id="primeplatinumpack1">
          <label class="container-radio">
            <input type="radio" name="radio" id="primeplatinumpack" onclick="paymentTypeDet(674);ajaxpayment('PRIMETUM12MONTHS');">
            <div class="radio-pack-text">PRIME - Till U Marry</div>
            <div class="radion-box-text1"><a href="javascript:void(0);" class="knowmore-button" onclick="know_more_smply('674', '463')">Know More <img src="https://mbobileshop.com/images/payment-revamp/knw-btn-arrow.svg?=v1" style="padding-left: 6px;"></a> </div>
                          <div class="radion-box-text2">
                <div>SAVE 68%</div>
              </div>
              <div>
                <span class="radion-box-greytext"><span>₹22,500</span></span>
                <span class="radion-box-greyblack">₹7,100</span></div>
                        <div class="checkmark"></div>
          </label>
        </div>
      </div>

      </div>
      <div style="border-top: 1px solid #333;width: 250px;margin: 21px auto 10px;"> <span style="position: absolute;margin-top: -8px;background: #fff;text-align: center;margin-left: 38px;width: 175px;">Offer Valid Only Today!</span></div>
      <div style="padding-top: 14px;padding-bottom: 7px;line-height: 16px;margin: 0 auto;display: block;text-align: center;">
        <button style="background-image: linear-gradient(to right, #de6722, #ea8d1f);background-color: #de6722;border: none;padding: 10px 76px 10px 76px;color: #ffffff;font-size: 14px;border-radius: 25px;font-family:Lato;text-decoration:none;letter-spacing: 0.42px;font-weight: bold;cursor: pointer;" onclick="getRedirectURl();ajaxpayment('SPAYNOW');">Pay Now ₹<span id="packpricedet">5,900</span></button>
      </div>
      <div style="color: #ed6402;text-align: center;margin-top:14px;"><a href="https://mbobileshop.com/payments/paymentoptionnew.php?gaact=PAY&gasrc=MENUSUB&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&referal=https://matches.MbobileShop.com/&gaact=PAY&gasrc=MENUSUB&OLDSCREEN=1" style="color: #ed6402;    text-decoration: none;" onClick="ajaxpayment('SVIEWALL');">View All Packages <img src="https://imgs.MbobileShop.com/webapp-assets/prof-compl-arw.svg"></a></div>
    </div>
  </div>
  <!-- Simplified payment End -->
  <!-- EPR Page Start -->
  <div class="simplify-payment" id="eprpayment" style="display:none;">
    <div>
      <div class="epr-payment-bg">

        <div class="epr-payment-bg-img">
          <span class="epr-payment-offer">Special Offer Just For You!</span>
          <span class="epr-payment-offer-perc">Save 0%</span>
        </div>
        <div class="epr-payment-offer-text">Offer Ends Today</div>
      </div>
       <!-- $GETDOMAININFO['domainnameshort'] == 'MbobileShop' --->
        <div class="mgb-img">
          <img src="https://imgs.MbobileShop.com/webapp-assets/revamp-images/money-back/mb-thumb-with-info.svg" height="94.73" width="422" alt="Money Back Guarantee" id="myBtn">
        </div>
            <div id="packbenefitdetepr">
      </div>
      <div class="epr-simplify-offer">
                  <div class="epr-offer-pack">0</div>
                <div style="margin-bottom: 10px;margin-top: 2px;">
          <span class="epr-offer-amount">₹ 0</span>
          <span class="epr-offer-perc">Save 0%</span>
        </div>
        <div>
          <span class="epr-offer-pack-amount"> ₹0 <span style="font-size: 16px;">for  Months  </span></span>

        </div>
      </div>
      <div style="padding-top: 10px;padding-bottom: 3px;line-height: 16px;margin: 0 auto;display: block;text-align: center;">
        <button style="background-image: linear-gradient(to right, #de6722, #ea8d1f);background-color: #de6722;border: none;padding: 10px 110px 10px 110px;color: #ffffff;font-size: 14px;border-radius: 25px;font-family:Lato;text-decoration:none;letter-spacing: 0.42px;font-weight: bold;cursor: pointer;" onclick="getRedirectURl();ajaxpayment('EPAYNOW')">Pay Now</button>
      </div>
      <div style="color: #ed6402;text-align: center;margin-top:14px;"><a href="https://mbobileshop.com/payments/paymentoptionnew.php?gaact=PAY&gasrc=MENUSUB&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&referal=https://matches.MbobileShop.com/&gaact=PAY&gasrc=MENUSUB&OLDSCREEN=1" style="color: #ed6402;    text-decoration: none;" onclick="ajaxpayment('EVIEWALL');">View All Packages <img src="https://imgs.MbobileShop.com/webapp-assets/prof-compl-arw.svg"></a></div>
    </div>
  </div>
  <!-- EPR Page End -->
      <div class="hpmainwraper pos-relative" id="packages-center-section1">
      <div class="inner-wrapper" style="width: 1300px;">
        <div class="paytoppromotxt"><span class="fntlarge">Get a flat Rs.3100 on 3 month Gold Pack</span> <span class="fntmedium">- Valid till 31-Jul-2025</span></div>
      </div>
    </div>
    <!---------:::::::::::::::::::::::::::SKIP BUTTON::::::::::::::::::::::::::::::::::::::::-->
    <!---------:::::::::::::::::::::::::::SKIP BUTTON::::::::::::::::::::::::::::::::::::::::-->
  <div class="hpmainwraper pos-relative">
    <div style=" margin: 0px auto;">
            <span id="packages-center-section" style="display: none;">
                  <!--- Payment Related Tabs Section start -->
                      <div class="mgb-img">
              <img src="https://imgs.MbobileShop.com/webapp-assets/revamp-images/money-back/mb-thumb-with-info.svg" height="94.73" onclick="paymentTypeDet(1)" width="422" alt="Money Back Guarantee" id="myBtn1">
            </div>
                    <div class="pay-page" style="float: none;margin: 0px auto 12px;display: block;overflow: hidden;border-bottom: 1px solid #cccccc;padding-top: 20px;cursor: pointer;">
            <div id="primepackage" onclick="paymentTypeDet(327);" class="membership_package" data-type="prime" style="float: left;color: #5f36bb;font-size: 16px;font-weight: bold;letter-spacing: 0.48px;cursor: pointer;height: 39px;">
              <img src="https://mbobileshop.com/images/payment-revamp/payment-prime-tabs-on.png" style="vertical-align: middle;padding-right: 3px;"> Packages
            </div>
            <div id="regularpackage" onclick="paymentTypeDet(1);" class="membership_package" data-type="regular" style="float: left;margin-left: 40px;font-size: 16px;letter-spacing: 0.48px;cursor: pointer;height: 39px;"><span style="position: relative;left: -6px;">Regular Packages</span>
            </div>
          </div>
          <!-- START MATRIMONY-319  -->
          <div id="package-prime-banner" style="display:none;">
            <img class="package-prime-banner" src="https://imgs.MbobileShop.com/bmimgs/desktop-images/pay-primebanners.png">
          </div>
          <!-- END MATRIMONY-319  -->
          <!--- Payment Related Tabs Section End -->
                <div class="fleft width-100 tabs-margin-bottom regulartab">
          <div class="inner-tabs-width">
            <div class="inner-tabs-border"></div>
            <div class="tabs-chip-width">
              <div class="tab chip-pad1" style="margin:0px auto;width:610px;margin-bottom:40px;">
                <div idval="3" class="tablinks update-chip-active" style="width:118px;margin-left:12px;height:36px;" id="3month">
                  <div class="update-chip-label" id="3label">3 Months
                  </div>
                </div>
                <div idval="6" class="tablinks update-chip-inactive" style="width:156px;margin-left:12px;height:36px;" id="6month">
                  <div class="inactivelabel" id="6label" style="padding: 18px;">
                    6 Months<IMG SRC="https://imgs.MbobileShop.com/bmimgs/payments/save-more-1.png?v=1" width="63" height="61" border="0" alt="Save More" style="vertical-align:middle;position:absolute;margin-top:-30px;margin-left:5px;"></div>
                </div>
                <div idval="12" class="tablinks update-chip-inactive" style="width:128px;margin-left:12px;height:36px;" id="12month">
                  <div class="inactivelabel" id="12label">
                    12 Months
                  </div>
                </div>
                <div idval="tum" class="tablinks update-chip-inactive" style="width:128px;margin-left:12px;height:36px;" id="tummonth">
                  <div class="inactivelabel till-marrychip" id="tumlabel">
                    Till U Marry
                    <span style="font-size: 12px;display: block;">Best Value</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="inner-tabs-border"></div>
          </div>
        </div>
        <!-- Add Arrows -->
        <div>
          <div class="swiper-button-prev package-swiper-button-prev" style="display:none;"></div>
        </div>
        <div>
          <div class="swiper-button-next package-swiper-button-next" style="float:left; margin-right:60px; display:none;"></div>
        </div>
        <div class="payment-cards swiper-container package-swiper-container s1" style="width: 1100px;margin:0px auto;">
          <div class="swiper-wrapper package-swiper-wrapper">
          </div>
        </div>
                <!-- START MATRIMONY-319  -->
                <div class="prime_eligible_terms_and_conditions" style="display:none;">
          *Prime access will be enabled once you add your photo and verify your profile				</div>
        <div class="assprime_eligible_terms_and_conditions" style="display:none;">
          **Subject to qualifying for Elite				</div>
        <div class="regular_eligible_terms_and_conditions" style="display:none;">
          * Terms & Conditions apply				</div>
        <!-- END MATRIMONY-319  -->
                  <div style="padding-top: 100px;text-align:center;"><img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-assisted-icon.png?v=1" width="198" height="141" border="0" alt="Assisted Service"></div>
          <div style="text-align:center;padding-bottom:20px;"><span style="font-weight:700;font-size: 19px;">Why paid membership?</span>
          </div>
          <div style="margin:0px auto;width:550px;height:150px;">
                          <div style="border-radius: 30px; background-image: linear-gradient(to bottom, #5cbb67, #1eb0c0); float:left;border-radius:50%;width:100px;height:100px;margin-right:50px;">
                <img src="https://imgs.MbobileShop.com/bmimgs/payments/assisted-call-icon.png?v=1" width="45" height="45" border="0" alt="Talk to matches directly" style="vertical-align:center;padding:27px 0px 30px 26px;">
                <div style="color:#000;font-size:14px;letter-spacing: 0.42px;text-align:center;width:104px;">Talk to matches directly</div>
              </div>
                          <div style="border-radius: 30px; background-image: linear-gradient(to bottom, #5cbb67, #1eb0c0); float:left;border-radius:50%;width:100px;height:100px;margin-right:50px;">
                <img src="https://imgs.MbobileShop.com/bmimgs/payments/assisted-details-icon.png?v=1" width="45" height="45" border="0" alt="Get complete profile details" style="vertical-align:center;padding:27px 0px 30px 26px;">
                <div style="color:#000;font-size:14px;letter-spacing: 0.42px;text-align:center;width:104px;">Get complete profile details</div>
              </div>
                          <div style="border-radius: 30px; background-image: linear-gradient(to bottom, #5cbb67, #1eb0c0); float:left;border-radius:50%;width:100px;height:100px;margin-right:50px;">
                <img src="https://imgs.MbobileShop.com/bmimgs/payments/assisted-visibility-icon.png?v=1" width="45" height="45" border="0" alt="Enhanced profile visibility" style="vertical-align:center;padding:27px 0px 30px 26px;">
                <div style="color:#000;font-size:14px;letter-spacing: 0.42px;text-align:center;width:104px;">Enhanced profile visibility</div>
              </div>
                          <div style="border-radius: 30px; background-image: linear-gradient(to bottom, #5cbb67, #1eb0c0); float:left;border-radius:50%;width:100px;height:100px;">
                <img src="https://imgs.MbobileShop.com/bmimgs/payments/assisted-responses-icon.png?v=1" width="45" height="45" border="0" alt="Get more responses" style="vertical-align:center;padding:27px 0px 30px 26px;">
                <div style="color:#000;font-size:14px;letter-spacing: 0.42px;text-align:center;width:104px;">Get more responses</div>
              </div>
                        <br clear="all">
          </div>
          <div style="margin:20px auto;text-align:center;"><a onclick="BestSeller()" class="continue_btn">Choose our best selling package</a>
          </div>
                                  <style>
            #eliteresponse {
              visibility: hidden;
              min-width: 250px;
              margin-left: -125px;
              background-image: linear-gradient(113deg, #5cbb67, #1eb0c0);
              color: #ffffff;
              text-align: center;
              border-radius: 2px;
              padding: 16px;
              position: fixed;
              z-index: 1;
              right: 3%;
              bottom: 30px;
              font-size: 15px;
            }

            #eliteresponse.show {
              visibility: visible;
              -webkit-animation: fadein 1.5s, fadeout 1.5s 2.5s;
              animation: fadein 1.5s, fadeout 1.5s 2.5s;
            }
          </style>
          <!-- Assisted Supreme Section Start -->
          <div id="AssistedSupreme" class="">
            <div style="padding-top: 50px;text-align:center;">
              <img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-assisted-service-img.png?v=1" width="304" height="152" border="0" alt="Assisted Service">
            </div>
            <div style="text-align:center;padding:25px 0px 10px 0px;"><span style="font-weight:700;font-size: 20px;">Assisted Supreme </span></div>
                          <div style="text-align:center;padding-bottom:5px;"><span style="font-size: 16px;color:#000;letter-spacing: 0.48px;">
                  A personalised matchmaking service Powered by MbobileShop</span></div>
              <div style="text-align: left;width: 567px;margin: 0 auto 15px;overflow: hidden;">
                                <div style="font-size: 16px;font-weight: bold;margin-top: 20px;letter-spacing: 0.48px;">Only MbobileShop offers these <span style='color: #3eb591;text-transform:uppercase;font-weight: 900;'>Exclusive</span> Assisted Supreme Service benefits</div>
                <div class="assisted-list-items">
                  <ul>
                                          <li>Dedicated Senior Relationship manager from your region, who understands your cultural nuances & speaks the language you are comfortable with</li>
                                          <li>Senior relationship manager shortlists and contacts prospects, schedules and facilitates video/direct calls with matches from India & abroad</li>
                                          <li>We offer a wider choice of matches from MbobileShop and CommunityMatrimony</li>
                                          <li>Prospects recommended to you are validated to ensure they are actively looking for a match</li>
                                          <li>Increased Profile Visibility in MbobileShop and CommunityMatrimony along with profile enhancements to get more responses</li>
                                          <li>First level horoscope matching with prospects</li>
                                          <li>Get all the benefits of Prime Gold package</li>
                                          <li>Get a chance to be part of our exclusive Elite database*</li>
                                                              <li>
                        <div style="font-weight:bold;">Service Guarantee!													<div class="tooltip" style="margin-left: 10px;margin-top: 0px;"><img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-question-icon.png">
                            <span class="tooltiptext">Within 15 days of the start of the service, if you are not happy we will refund your entire payment. No questions asked!</span>
                          </div>
                        </div>
                        <div style="padding-top: 10px;float: left;width: 85%;">We are quite confident of bringing the right matches to you. However, if you are not happy with our service, we will give your money back. No questions asked!</div>
                        <div style="padding-top: 10px;float: left;width: 15%;text-align: right;"><img src="https://imgs.MbobileShop.com/bmimgs/assisted/assisted-service-gurantee.svg"></div>
                      </li>
                                      </ul>
                </div>
              </div>
                        <div style="text-align:center;padding:15px 0px 0px 0px;font-size: 12px;color: #777777;letter-spacing: 0.42px;">*Subject to qualifying for Elite
            </div>
            <div style="text-align:center;padding:25px 0px 18px 0px;"><span style="font-weight:700;font-size: 16px;">Select an Assisted Supreme Package</span>
            </div>
                          <div style="margin:0px auto;text-align:center;width:1200px;">
                <ul style="list-style:none;margin:0px;padding:0px;">
                  <li class="assisted-tab active" onclick="AssistedPackage(361)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;margin-right:10px;color: #ff9800;">3 Months</li>
                  <li class="assisted-tab" onclick="AssistedPackage(362)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;margin-right:10px;color: #ff9800;">6 Months</li>
                  <li class="assisted-tab" onclick="AssistedPackage(363)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;color: #ff9800;">12 Months</li>
                </ul>
              </div>
                      </div>
          <!-- Assisted Supreme Section End -->
          <div id="AssistedServiceSection" class="">
            <div style="padding-top: 50px;text-align:center;">
                              <img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-assisted-service-img.png?v=1" width="304" height="152" border="0" alt="Assisted Service">
                          </div>
            <div style="text-align:center;padding:25px 0px 10px 0px;"><span style="font-weight:700;font-size: 20px;">Assisted Service</span></div>
                          <div style="text-align:center;padding-bottom:5px;"><span style="font-size: 16px;color:#000;letter-spacing: 0.48px;">
                  A personalised matchmaking service Powered by MbobileShop</span></div>
              <div style="text-align: left;width: 567px;margin: 0 auto 15px;overflow: hidden;">
                                <div style="font-size: 16px;font-weight: bold;margin-top: 20px;letter-spacing: 0.48px;">Only MbobileShop offers these <span style='color: #3eb591;text-transform:uppercase;font-weight: 900;'>Exclusive</span> Assisted Service benefits</div>
                <div class="assisted-list-items">
                  <ul>
                                          <li>We offer a wider choice of matches from both MbobileShop and CommunityMatrimony</li>
                                          <li>Increased profile visibility in both MbobileShop and CommunityMatrimony along with profile enhancements to get more responses</li>
                                          <li>Dedicated Relationship Manager from your region, who understands your cultural nuances & speaks the language you are comfortable with</li>
                                          <li>Relationship Manager shortlists and contacts prospects, schedules and facilitates video calls/direct meetings with them</li>
                                          <li>First level of horoscope matching with prospective matches while shortlisting their profiles</li>
                                                              <li>
                        <div style="font-weight:bold;">Service Guarantee!													<div class="tooltip" style="margin-left: 10px;margin-top: 0px;"><img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-question-icon.png">
                            <span class="tooltiptext">Within 15 days of the start of the service, if you are not happy we will refund your entire payment. No questions asked!</span>
                          </div>
                        </div>
                        <div style="padding-top: 10px;float: left;width: 85%;">We are quite confident of bringing the right matches to you. However, if you are not happy with our service, we will give your money back. No questions asked!</div>
                        <div style="padding-top: 10px;float: left;width: 15%;text-align: right;"><img src="https://imgs.MbobileShop.com/bmimgs/assisted/assisted-service-gurantee.svg"></div>
                      </li>
                                      </ul>
                </div>
              </div>
                        <div style="text-align:center;padding:25px 0px 18px 0px;"><span style="font-weight:700;font-size: 16px;">Select an Assisted Package</span>
            </div>
                          <div style="margin:0px auto;text-align:center;width:1200px;">
                <ul style="list-style:none;margin:0px;padding:0px;">
                  <li class="assisted-tab active" onclick="AssistedPackage(48)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;margin-right:10px;color: #ff9800;">3 Months</li>
                  <li class="assisted-tab" onclick="AssistedPackage(80)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;margin-right:10px;color: #ff9800;">6 Months</li>
                  <li class="assisted-tab" onclick="AssistedPackage(306)" style="font-size:14px;letter-spacing: 0.42px;padding:12px 24px;display:inline-block;color: #ff9800;">12 Months</li>
                </ul>
              </div>
                      </div>
                          <div class="payment-success-box">
            <div style="text-align:center;padding:88px 0px 8px 0px;">
              <div style="font-size: 20px;color:#000;letter-spacing: 0.6px;font-weight:700;width: 44%;margin: 0 auto;">Featured in Limca Book of World Records for highest number of documented marriages online<br/></div>
            </div>
            <div style="text-align:center;padding-bottom:32px;"><span style="font-size: 16px;color:#000;letter-spacing: 0.48px;">Some of our recent success stories</span>
            </div>
            <!-- Add Arrows -->
            <div style="position: absolute;top: 83%;left: 9%;">
              <div class="swiper-button-prev success-swiper-button-prev"></div>
            </div>
            <div style="position: absolute;top: 83%;right: 11%;">
              <div class="swiper-button-next success-swiper-button-next" style="float:left; margin-right:30px;"></div>
            </div>
            <div class="swiper-container s2" style="width: 827px;margin:0px auto;">
              <div class="swiper-wrapper" style="width: 827px;margin:0px auto;">
                                  <div class="swiper-slide payment-ss-content">
                    <div class="payment-ss-img"><img src="https://imgs.MbobileShop.com/bmimgs/arun-priya-bm-upg-ss720.png?v=1" width="250" height="150"></div>
                    <div class="payment-ss-text">
                      <span class="payment-ss-text1">Arun & Priya</span>
                      <span class="payment-ss-text2"></span>
                    </div>
                  </div>
                                  <div class="swiper-slide payment-ss-content">
                    <div class="payment-ss-img"><img src="https://imgs.MbobileShop.com/bmimgs/bijin-shruthi-bm-upg-ss720.png?v=1" width="250" height="150"></div>
                    <div class="payment-ss-text">
                      <span class="payment-ss-text1">Bijin Muralidharn & Shruthi</span>
                      <span class="payment-ss-text2"></span>
                    </div>
                  </div>
                                  <div class="swiper-slide payment-ss-content">
                    <div class="payment-ss-img"><img src="https://imgs.MbobileShop.com/bmimgs/krishnamohan-anagha-bm-upg-ss720.png?v=1" width="250" height="150"></div>
                    <div class="payment-ss-text">
                      <span class="payment-ss-text1">Krishnamohan & Anagha Tharur</span>
                      <span class="payment-ss-text2"></span>
                    </div>
                  </div>
                              </div>
            </div>
            <div class="payment-success-button">
              <!--<a href="#" class="payment-ss-button"><img src=".png"> Become a Premium Member</a>-->
              <a href="javascript:;" onclick="BecomePremium(1)" class="payment-ss-button"><img src="https://mbobileshop.com/images/payment-revamp/payment-crown-icon.svg?=v1" style="vertical-align: middle;margin-right: 6px;">Become a Paid Member</a>
            </div>
          </div>
                        <div style="margin:0px auto;text-align:center;">
          <div class="payment-query-box">
            <div style="text-align:center;">
              <div style="width:420px;float:left;font-size: 16px;color:#000;letter-spacing: 0.6px;font-weight:700;padding:30px 0px 0px 116px;">Have any queries or need help in making payment?</div>
              <div style="margin:0px auto;text-align:center;float:left;padding:16px 0px;">
                <ul style="list-style:none;margin:0px;padding:0px;margin-top:8px;">
                  <li  onClick="ChatWithUS()"  class="" style="font-size:14px;letter-spacing: 0.42px;padding:4px 8px;display:inline-block;margin-right:10px;border-radius: 8px;border: solid 1px #777777; cursor: pointer;"><img src="https://imgs.MbobileShop.com/bmimgs/payments/payment-help-chat-icon.png?v=1" width="24" height="24" border="0" alt="Chat with us" style="vertical-align:middle;padding-right:4px;">Chat with us</li>
                                  </ul>
              </div>
            </div>
          </div>
        </div>
      </span>
    </div>
            <div style="margin:0px auto;width: 950px;height:75px;padding-top:55px;/* margin-right: 300px; */">
      <ul style="list-style:none;margin:0px;padding:0px;">
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-vbv-icon.png?v=1') no-repeat;vertical-align:middle;width:90px; height:43px;margin-right:50px;float:left;"></li>
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-master-icon.png?v=1') no-repeat;vertical-align:middle;width:104px;height:45px;margin-right:50px;float:left;"></li>
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-pci-icon.png?v=1') no-repeat;vertical-align:middle;width:125px;height:47px;margin-right:50px;float:left;"></li>
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-trustwave-icon.png?v=1') no-repeat;vertical-align:middle;width:88px;height:45px;margin-right:50px;float:left;"></li>
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-safekey-icon.png?v=1') no-repeat;vertical-align:middle;width:115px;height:36px;margin-right:50px;float:left;"></li>
        <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-verisign-icon.png?v=1') no-repeat;vertical-align:middle;width:122px;height:41px;margin-right:50px;float:left;"></li>
        <!-- <li style="background:url('https://imgs.MbobileShop.com/bmimgs/payments/payment-footer-paypal-icon.png?v=1') no-repeat;vertical-align:middle;width:120px;height:31px;float:left;"></li> -->
      </ul>
    </div>
      </div>
  </div>
    <div class="hpmainwraper pos-relative">
    <div class="inner-wrapper">
      <div style="background:#f1f1f1;height: 2px;;"><img src="https://imgs.bengalimatrimony.com/bmimgs/trans.gif" height="2" alt="MbobileShop" /></div>
      <div style="margin-top:30px;letter-spacing: 0.36px;font-size: 15px;color:#000;text-align:center;">Copyright &copy; 2025 All rights reserved.
      </div>
    </div><br clear="all">
  </div>
    <script src="https://mbobileshop.com/scripts/swiper-bundle.min.js"></script>
  <!-- Initialize Swiper -->
  <script type="text/javascript" language="javascript" src="https://mbobileshop.com/scripts/jquery.js"></script>
  <script type="text/javascript" language="javascript" src="https://mbobileshop.com/scripts/regpaymentoptionspage.js?q=19022020"></script>
  <script type="text/javascript" src="https://mbobileshop.com/payments/ajax_paymenttrack.php?MatriId=H14550547&promolink=0&referer_source=https://matches.MbobileShop.com/&cn=98&promolink=&pageload=1&segmentuser=4&createddays=88&displaygamooga=1"></script>	<script type="text/javascript">
    function updateTimer() {
    var offerEndDate = "";
    const targetDate = new Date(offerEndDate);
    let now = new Date();
    let remainingTime = targetDate - now;

    // Calculate days, hours, minutes, and seconds
    let days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
    let hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    if(hours.toString().length == 1){
      hours = "0"+hours;
    }
    if(minutes.toString().length == 1){
      minutes = "0"+minutes;
    }
    if(seconds.toString().length == 1){
      seconds = "0"+seconds;
    }

    var hoursdigits = hours.toString().split('');
    var minutesdigits = minutes.toString().split('');
    var secondsdigits = seconds.toString().split('');
    // Display the result
    document.getElementById("timer").innerHTML = '<div class="timer-section sub-heading-two"><div class="timer-subsection"><span><span class="timer-box">'+hoursdigits[0]+'</span><span class="timer-box ml-2">'+hoursdigits[1]+'</span></span><span class="caption hour-sec-text">HH</span></div> <span class="column-cls">:</span><div class="timer-subsection"><span><span class="timer-box">'+minutesdigits[0]+'</span><span class="timer-box ml-2">'+minutesdigits[1]+'</span></span><span class="caption hour-sec-text">MM</span></div> <span class="column-cls">:</span><div class="timer-subsection"><span><span class="timer-box">'+secondsdigits[0]+'</span><span class="timer-box ml-2">'+secondsdigits[1]+'</span></span><span class="caption hour-sec-text">SS</span></div></div>';

    // Check if the countdown is finished
    if (remainingTime < 0) {
      clearInterval(timerInterval);
      document.getElementById("timer").innerHTML = '<div class="timer-section sub-heading-two"><div class="timer-subsection"><span><span class="timer-box">0</span><span class="timer-box ml-2">0</span></span><span class="caption hour-sec-text">HH</span></div> <span class="column-cls">:</span><div class="timer-subsection"><span><span class="timer-box">0</span><span class="timer-box ml-2">0</span></span><span class="caption hour-sec-text">MM</span></div> <span class="column-cls">:</span><div class="timer-subsection"><span><span class="timer-box">0</span><span class="timer-box ml-2">0</span></span><span class="caption hour-sec-text">SS</span></div></div>';
    }
  }
    //  START MATRIMONY-319
    $("#prime_tooltip_gotit").click(function() {
      $("#prime_tooltip").css("display", "none");
      $('.tooltip-addon').removeAttr('id');
    });
    //  END MATRIMONY-319
    var scriptloaded = 0;
    var matriid = 'H14550547';
    var _ss_track = {};
    /* your customization options */
    _ss_track.options = {};
    var ss = document.createElement('script');

    function gamoogascriptload() {
      console.log(":::::::::::::::::::::Gamoooga script loaded:::::::::::::::::::::::::::::::");
      if (scriptloaded == 0) {
        scriptloaded = 1;
        /*::::::::::::::::::::::::::::::::SS Track ::::::::::::::::::::::::::::::::::::*/
                  /* Donot edit below this line */
          _ss_track.id = "206f307a-c1bf-41ec-8ac6-8d0b3a07ace5";
          _ss_track.events = [];
          _ss_track.handlers = [];
          _ss_track.alarms = [];
          (function() {
            ss.type = 'text/javascript';
            ss.async = true;
            ss.id = "__ss";
            ss.src = '//gsecondscreen.matrimonycdn.com/static/ssclient.min.js?matriid=' + matriid;
            var fs = document.getElementsByTagName('script')[0];
            fs.parentNode.insertBefore(ss, fs);
          })();
          /*::::::::::::::::::::::::::::::::SS Track ::::::::::::::::::::::::::::::::::::*/
                console.log(":::::::::::::::::::::ss:::::::::::::::::::::::::::::::");
        console.log(ss);
      }
    }
  </script>
  <script>
    /*::::::::::::::::::::::::::::::::Variable Initalization ::::::::::::::::::::::::::::::::::::*/
    var MonthArray = {
      '3': 90,
      '6': 180,
      '12': 365,
      'tum': 365
    };
    var MonthArrayPkg = {
      '3': ['1','48','327','443','599','361'],
      '6': ['2','80','328','444','600','362'],
      '12': ['329','445','601','363','436','306'],
      'tum': ['673','674','675','676']
    };
    var MonthlyBasedArray = {
      'CLASSIC1': 1,
      'CLASSIC3': 3,
      'CLASSIC6': 6,
      'CLASSICADV3': 3,
      'CLASSICADV6': 6,
      'CLASSICPRE3': 3,
      'CLASSICPRE6': 6,
      'ASSISTED3': 3,
      'ASSISTED6': 6,
      'ASSISTED12': 12,
      'TILLUMARRYREG': 12,
      'TILLUMARRYADD': 12,
      'TWINPACK3': 3,
      'TWINPACKTUM': 12,
      'TWINPACK6': 6,
      'PRIMEPLUS3': 3,
      'PRIMEPLUS6': 6,
      'PRIMEPLUS12': 12,
      'TWINPRIME3': 3,
      'TWINPRIME6': 6,
      'TWINPRIME12': 12,
      'ASSISTEDS3': 3,
      'ASSISTEDS6': 6,
      'ASSISTEDS12': 12,
      'ASSISTEDPRIME3': 3,
      'ASSISTEDPRIME6': 6,
      'ASSISTEDPRIME12': 12
    };
    var package_type_array = {
      322: 'CLASSIC1',
      1: 'CLASSIC3',
      2: 'CLASSIC6',
      3: 'CLASSIC9',
      4: 'CLASSICADV3',
      5: 'CLASSICADV6',
      6: 'CLASSICADV9',
      13: 'CLASSICPRE3',
      14: 'CLASSICPRE6',
      49: 'CLASSICPRE9',
      48: 'ASSISTED3',
      80: 'ASSISTED6',
      306: 'ASSISTED12',
      237: 'TILLUMARRYREG',
      238: 'TILLUMARRYADD',
      266: 'TWINPACK3',
      267: 'TWINPACKTUM',
      288: 'TWINPACK6',
      327: 'PRIMEPLUS3',
      328: 'PRIMEPLUS6',
      329: 'PRIMEPLUS12',
      433: 'TWINPRIME3',
      434: 'TWINPRIME6',
      435: 'TWINPRIME12',
      361: 'ASSISTEDS3',
      362: 'ASSISTEDS6',
      363: 'ASSISTEDS12',
      599: 'ASSISTEDPRIME3',
      600: 'ASSISTEDPRIME6',
      601: 'ASSISTEDPRIME12'
    }
    var DomainShort = 'MbobileShop';
    var PageType = DomainShort + ' Reg Payment Page New';
    var Benefitsiconjson = '{"chaticon":"unlimited_chat","messageicon":"unlimited_chat","mobileicon":"pay-icon-4","phoneicon":"view_mob","matchesicon":"pay-icon-4","benefiticon":"pay-icon-5","horoscopeicon":"pay-icon-2","highlightericon":"highlighter","astroicon":"pay-icon-7","premiumicon":"pay-icon-4","visibilityicon":"pay-icon-4","relationshipicon":"pay-icon-3","understandsicon":"pay-icon-10","handpicksicon":"pay-icon-6","AddOnOffer":"pay-extra-percentage-icon","premium":"premium","videoicon":"videoicon","prospecticon":"pay-icon-11","allbenefiticon":"pay-icon-12","freeaddonicon":"pay-icon-13","exclusiveeliteicon":"pay-icon-14","payprimerelationship":"pay-prime-relationship-icon","moremessageicon":"icon-more-messages","premiumcrownicon":"icon-premium-crown"}';
    var jsonresponse = '{"MOBILENO":"MDYgJTU6NyQnMw==","EMAILID":"emRxfGRkfiYjRWZ\/YGJkJ2J9ew==","ASSISTEDASSUREDPACKTERMSCONDITION":"* Meeting can be virtual, telephonic or in-person","ASSISTEDASSUREDPACKSHOWFLAG":"0","NUMBEROFPAYMENT":"0","DAYSLEFT":"0","PRIME_ENABLE":"1","DOORSTEP_ENABLE":"0","PRIME_PAYMENT_NOTIFICATION":{"COUNT":"5","CONTENT":"We recommend PRIME packages to contact 100% ID-verified, genuine, and high-quality matches from the PRIME section. You also get all the benefits of regular packages."},"PRIME_PAYMENT_OFFER_BANNER":"pay-primebanners-new.svg","PRIME_PAYMENT_TERMS_AND_CONDITIONS":"*Prime access will be enabled once you add your photo and verify your profile","ASSISTEDPRIME_PAYMENT_TERMS_AND_CONDITIONS":"**Subject to qualifying for Elite","TWINPRIME_ENABLE":"1","PROFILE":{"STATUS":"0","VALIDATED":"1","EXPDATE":"","ENTRYTYPE":"F","LASTPAYMENT":"0000-00-00 00:00:00","VALIDDAYS":"0","NUMBEROFPAYMENTS":"0","OFFERAVAILABLE":"0","COUNTRYSELECTED":"98","LOGINCOUNT":"46","DISCOUNT_CREATION_DAYS":"89","LASTONLINEPAYMENTPRODUCTID":"0","DEFAULTVIEW":"1","SPECIALPRIV":"0","AUTORENEWALSTATUS":"0","EXPIRYDATE":"0000-00-00 00:00:00","TIMECREATED":"2025-05-02 04:20:38","GENDER":"M","RELIGION":"8","AGE":"47","DAYOFBIRTH":"21","MONOFBIRTH":"12","YEAROFBIRTH":"1977","MARITALSTATUS":"1","MOTHERTONGUE":"17","CASTE":"0","SUBCASTEID":"0","OCCUPATIONSELECTED":"888","OCCUPATIONCATEGORY":"5","BODYTYPE":"0","PHOTOAVAILABLE":"1","PENDINGPHOTOVALIDATION":"0","DOSHAM":"0","EDUCATIONID":"47","ANNUALINCOME":"0","RESIDINGDISTRICT":"314","BYWHOM":"10","COUNTRY":"IN","IPLOCATION":"98"},"PACKAGE_OFFER":{"MEMBERDISCOUNTINRFLATRATE":"1~3100|2~6100|48~3000|80~5400|266~4800|288~9200|306~9000|327~4400|328~9000|361~2100|362~2800|363~5100|433~7100|434~13500|443~4300|444~8900|599~4000|600~7300|601~12100|673~11000|674~15400|675~16900|676~24200","MEMBERDISCOUNTUSDFLATRATE":"1~25|2~58|48~80|80~140|266~38|288~87|306~235|327~45|328~102|361~40|362~50|363~90|433~67|434~153|443~61|444~136|599~85|600~150|601~255|673~140|674~219|675~211|676~329","MEMBERDISCOUNTEUROFLATRATE":"1~21|2~49|266~31|288~74|327~40|328~88|433~60|434~132|443~54|444~121|673~122|674~197|675~182|676~296","MEMBERDISCOUNTAEDFLATRATE":"1~107|2~237|48~290|80~520|266~160|288~355|306~860|327~163|328~361|361~140|362~190|363~340|433~244|434~541|443~220|444~492|599~310|600~560|601~940|673~532|674~814|675~797|676~1221","MEMBERDISCOUNTGBPFLATRATE":"1~20|2~44|266~30|288~66|327~35|328~77|433~53|434~116|443~46|444~103|673~106|674~168|675~158|676~254","MEMBERDISCOUNTMYRFLATRATE":"1~108|2~240|266~163|288~361|327~191|328~448|433~286|434~672","OFFERCATEGORYID":"6666","OFFERCODE":"66661014550547","OFFERENDDATE":"2025-07-31 05:59:59","OFFERSTARTDATE":"2025-07-30 00:00:00","MEMBERASSUREDGIFT":"","ADDON_FLATRATE_ENABLED":"0","GSTINCLUSIVE":"","ASSUREDGIFTSELECTED":"0"},"PKGMOSTPOPULAR":"4","PRIMEPKGMOSTPOPULAR":"327","GAMOOGA":{"TIMER":"3600000","TIMERT2":"25000","DISABLED":"1","EDUDET":"47"},"PREMIUM_MEMBERSHIP":{"PREMIUMMEMBERSHIPINTROCONTENT":"Why paid membership?","PREMIUMMEMBERSHIPMAINIMAGE":"pay-premium-icom.png","PREMIUMMEMBERSHIPLIST":"Talk to matches directly~Get complete profile details~Enhanced profile visibility~Get more responses@^@assisted-call-icon.png~assisted-details-icon.png~assisted-visibility-icon.png~assisted-responses-icon.png","PREMIUMMEMBERSHIPBTNLABEL":"Choose our best selling package"},"DOMAIN":"MbobileShop","ELITE_MEMBER_FLAG":"0","SERVICE":{"SERVICEHEADING":"Assisted Service","SERVICEINTROCONTENT":"A personalised matchmaking service Powered by MbobileShop","SERVICESUBHEADING":"Only MbobileShop offers these @exclusive@ Assisted Service benefits","SERVICELIST":"We offer a wider choice of matches from both MbobileShop and CommunityMatrimony~Increased profile visibility in both MbobileShop and CommunityMatrimony along with profile enhancements to get more responses~Dedicated Relationship Manager from your region, who understands your cultural nuances & speaks the language you are comfortable with~Relationship Manager shortlists and contacts prospects, schedules and facilitates video calls\/direct meetings with them~First level of horoscope matching with prospective matches while shortlisting their profiles","SERVICELASTLIST":"Service Guarantee!~We are quite confident of bringing the right matches to you. However, if you are not happy with our service, we will give your money back. No questions asked!~image","SERVICEFOOTCONTENT":"Select an Assisted Package","SERVICEMAINIMAGE":"assisted-service-top-img.svg","ELITETOASTERCONTENT":"Thank you for your interest. We will get in touch with you shortly","SERVICEQUESTIONTEXT":"Within 15 days of the start of the service, if you are not happy we will refund your entire payment. No questions asked!"},"ASSSERVICE":{"SERVICEHEADING":"Assisted Supreme Service","SERVICEINTROCONTENT":"A personalised matchmaking service Powered by MbobileShop","SERVICESUBHEADING":"Only MbobileShop offers these @exclusive@ Assisted Supreme Service benefits","SERVICELIST":"Dedicated Senior Relationship manager from your region, who understands your cultural nuances & speaks the language you are comfortable with~Senior relationship manager shortlists and contacts prospects, schedules and facilitates video\/direct calls with matches from India & abroad~We offer a wider choice of matches from MbobileShop and CommunityMatrimony~Prospects recommended to you are validated to ensure they are actively looking for a match~Increased Profile Visibility in MbobileShop and CommunityMatrimony along with profile enhancements to get more responses~First level horoscope matching with prospects~Get all the benefits of Prime Gold package~Get a chance to be part of our exclusive Elite database*","SERVICELASTLIST":"Service Guarantee!~We are quite confident of bringing the right matches to you. However, if you are not happy with our service, we will give your money back. No questions asked!~image","SERVICEFOOTCONTENT":"Select an Assisted Supreme Package","SERVICEMAINIMAGE":"assisted-service-top-img.svg","ELITETOASTERCONTENT":"Thank you for your interest. We will get in touch with you shortly","SERVICEQUESTIONTEXT":"Within 15 days of the start of the service, if you are not happy we will refund your entire payment. No questions asked!"},"SUCCESS_STORIES":{"SUCCESSSTORIESHEADING":"Featured in Limca Book of World Records for highest number of documented marriages online.","SUCCESSSTORIESINTROCONTENT":"Some of our recent success stories","SUCCESSSTORIESIMAGES":"arun-priya-bm-upg-ss720.png~bijin-shruthi-bm-upg-ss720.png~krishnamohan-anagha-bm-upg-ss720.png","SUCCESSSTORIESNAMES":"Arun & Priya~Bijin Muralidharn & Shruthi~Krishnamohan & Anagha Tharur","SUCCESSSTORIESPOSTEDON":"","SUCCESSSTORIESBTNLABEL":"Become a Paid Member"},"CONTACT_US":{"CONTACTUSCONTENT":"Have any queries or need help in making payment?"},"EEFCACCOUNTDETAILS":{"ACCOUNT NAME":"Matrimony.com Limited","A\/C NUMBER":"03862430000113","TYPE":"EEFC","CURRENCY":"USD","BANK NAME":"HDFC Bank Ltd.","BRANCH":"Santhome","IFSC CODE":"HDFC0000386","SWIFT CODE":"HDFCINBBCHE","CURRESPONDENT BANK":"USD: JPMorgan Chase Bank, New York","CURRESPONDENT <BR>A\/C NUMBER":" 001-1-406717","ADDITIONAL A\/C DETAILS":"CHIPS ABA:0002","CORRESPONDENT BANK\u2019S SWIFT CODE":"CHASUS33"},"PAYMENTASSOCIATESLIST":["Kuwait","Bahrain","Qatar","Saudi Arabia"],"PAYMENTASSOCIATES":{"KUWAIT":{"CITYNAME":"Kuwait","NAME":"Joseph","ADDRESS":"Behind Dasma Co-operative, Dasma - 112, Kuwait.","PHONE":"965-6078301."},"BAHRAIN":{"CITYNAME":"Bahrain","NAME":"Mohamed Elias","ADDRESS":"OLOUF TRAVELS, Al Gudaibiya, Kingdom of Bahrain.","PHONE":"00973 - 39292003."},"QATAR":{"CITYNAME":"Qatar","NAME":"Rimzan","ADDRESS":"P.O. BOX 201775, Doha - Qatar.","PHONE":"00974-30529719."},"SAUDI ARABIA":{"CITYNAME":"Saudi Arabia","NAME":"Saudi Arabia","ADDRESS":"Dammam, Saudi Arabia - 12354.","PHONE":"966561521598.","NAME1":"A B Thilakan","ADDRESS1":"Post.Box.No.266, AL Khobar, <br>King Fahad Street, 8th Cross, Dammam,<br \/> Saudi Arabia - 31952.","PHONE1":"966502000686."},"OMAN":{"CITYNAME":"Oman","NAME":"N.S. Ibrahim","ADDRESS":"Post.Box.No.31 & Post Code: 122, Mabelah, S. OF OMAN.","PHONE":"00968 - 92904517."}},"OFFERENDDATE":"2025-07-31 05:59:59","SEGMENTTYPE":"","IOSTHIRDPARTYENABLE":"0","CARDPAGEREDIRECTURL":"https:\/\/MbobileShop.com\/payments\/mobpaymentmode.php?bmck=8&ts=1753847039","PKGCURRENCYCODE":"INR","SOLARFOLDERSELECT":"Saturday22","PRIME_PACKAGE":["327","328","329","443","444","445","599","600","601","361","362","363","674","433","434","435","676"],"ADDONOFFERPKGINFO":"1~90~0","PAYMENTPAGELANDINGDATA":"0","GBPSNRI":"0","SIMPLIFIEDPAGE":{"FLAG":"1","FESBANIMAGE":"","TITLE":"Become a paid member","HEADING":"Pay now to contact matches","BESTSELLINGPKGID":"327","PKG":[{"PKGID":"1","PKGNAME":"Gold","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"5300","PKGDISCOUNTEDRATE":"3100","PKGRATE":"2200","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat,<\/span> view <span class=font-weight-bold>50 verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>~@#@View and contact <span class=font-weight-bold>ID verified matches with photos<\/span> from <span class=font-weight-bold>exclusive Prime section<\/span>~@#@<span class=font-weight-bold>Priority customer service <\/span>helpline~@#@Get <span class=font-weight-bold>better visibility and responses <\/span>from matches with 1-month Profile Highlighter","PERCENTAGE":"58","PKGTRACKID":"252","PKGSERVICES":"BASIC"},{"PKGID":"327","PKGNAME":"Prime Gold","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"7500","PKGDISCOUNTEDRATE":"4400","PKGRATE":"3100","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat,<\/span> view <span class=font-weight-bold>unlimited verified mobile numbers<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>~View and contact <span class=font-weight-bold>ID verified matches with photos<\/span> from <span class=font-weight-bold>exclusive Prime section<\/span>~<span class=font-weight-bold>Priority customer service <\/span>helpline~@#@Get <span class=font-weight-bold>better visibility and responses <\/span>from matches with 1-month Profile Highlighter","PERCENTAGE":"59","PKGTRACKID":"253","PKGSERVICES":"BASIC"},{"PKGID":"674","PKGNAME":"Prime Till U Marry","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"22500","PKGDISCOUNTEDRATE":"15400","PKGRATE":"7100","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat,<\/span> view <span class=font-weight-bold>unlimited verified mobile numbers<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>~View and contact <span class=font-weight-bold>ID verified matches with photos<\/span> from <span class=font-weight-bold>exclusive Prime section<\/span>~<span class=font-weight-bold>Priority customer service <\/span>helpline~@#@Get <span class=font-weight-bold>better visibility and responses <\/span>from matches with 1-month Profile Highlighter","PERCENTAGE":"68","PKGTRACKID":"457"}],"PAYNOWBUTTONTRACKNO":"260"},"EPRPAYMENTPAGE":{"FLAG":"0","OFFER":{"BGIMG":"https:\/\/imgs.MbobileShop.com\/webapp-assets\/images\/payment\/pay-epr-offer-img.svg","CONTENT":"Special Offer Just For You!","ENDDATECONTENT":"Offer Ends Today"},"HEADING":"Become a paid member to contact matches","PAYNOWBUTTONTRACKNO":"264"},"RENEWPAYMENTPAGE":{"FLAG":"0","OFFER":"","TITLE":"","HEADING":"","PKG":"","RENEWMATCH":"","BESTSELLINGPKGID":"327","PACKCNT":"","EXPIRESTATUS":""},"EXPLORESECTION":{"FLAG":"0","PKG":"","TITLE":"Benefits of Prime Gold Package","PAYNOWBUTTONTRACKNO":"342"},"RESPONSECODE":"1","ERRCODE":"0","TWINPACKFLAG":"1","TWINPACKTITLE":"Double Membership benefits of MbobileShop & 40plus at single price!","OFFERTXT":"","PAYMENTHELPLINE":{"PHONENO1":"","PHONENO2":""},"GSTPERC":"18","PAYTMPAY":"0","RAZORPAYUPI":"0","CURATEDFLAG":"0","TOTALPKG":"40","PKGCURRENCY":"\u20b9","QUICKCHECKOUTLANDING":"0","UPIPG":"2","VPAMODE":"2","ISCAMPAIGNTRACKENABLED":"1","CARDRENEWALFLAG":"1","RECURRINGFLAGENABLE":"0","CHECKOUTADDONINFO":"Profile Highlighter for 15 Days~350","PACKAGELIST":[{"PACKAGENAME":"3 MONTHS"},{"PACKAGENAME":"6 MONTHS"},{"PACKAGENAME":"12 MONTHS"}],"PKGINFO":{"PKG":[{"PKGID":"1","PKGNAME":"Gold","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"5300","PKGDISCOUNTEDRATE":"3100","PKGRATE":"2200","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Initiate conversations with matches, send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> 50 verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon","PKGPHONECOUNT":"50","PKGSMSCOUNT":"30"},{"PKGID":"2","PKGNAME":"Gold","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"9500","PKGDISCOUNTEDRATE":"6100","PKGRATE":"3400","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Initiate conversations with matches, send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> 100 verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~highlightericon","PKGPHONECOUNT":"100","PKGSMSCOUNT":"60"},{"PKGID":"3","PKGNAME":"Gold","PKGDURATION":"270","PKGEXTRADURATION":"0","PKGACTUALRATE":"8600","PKGDISCOUNTEDRATE":"0","PKGRATE":"8600","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"","PKGBENIFITIMG":"","PKGPHONECOUNT":"120","PKGSMSCOUNT":"90"},{"PKGID":"48","PKGNAME":"Assisted Gold","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"24900","PKGDISCOUNTEDRATE":"3000","PKGRATE":"21900","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span> shortlists, connects with relevant matches and arranges meetings~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All benefits of Gold Package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"25","PKGSMSCOUNT":"30"},{"PKGID":"80","PKGNAME":"Assisted Gold","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"44800","PKGDISCOUNTEDRATE":"5400","PKGRATE":"39400","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span> shortlists, connects with relevant matches and arranges meetings~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All benefits of Gold Package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"50","PKGSMSCOUNT":"60"},{"PKGID":"673","PKGNAME":"Gold Till U Marry","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"15900","PKGDISCOUNTEDRATE":"11000","PKGRATE":"4900","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Initiate conversations with matches, send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> Unlimited Mobile Numbers*<\/span> <div style=display:inline-block;><div style=display:none; class=UNLIMITED_CONTACT_NO_BENEFITS_POPUP673><div class=benefits-prime-tooltip><span class=benefits-info-close onclick=closePrimeBenefitsInfo(673)><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/images\/close-icon-black.svg \/><\/span><div class=benefits-info-list><span class=benefits-info-title d-block>View unlimited phone numbers of the accepted prospects<\/span><\/div><\/div><div class=white-overlay-prime><\/div><\/div><\/div><span onclick=openPrimeBenefitsInfo(673) class=benefits-info-icon><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/revamp-images\/tool-tip-icon.svg style=vertical-align:middle;cursor:pointer;> <\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon","PKGPHONECOUNT":"100","PKGSMSCOUNT":""},{"PKGID":"266","PKGNAME":"Combo","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"8000","PKGDISCOUNTEDRATE":"4800","PKGRATE":"3200","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with members on both <span class=font-weight-bold>MbobileShop<\/span> and <span class=font-weight-bold>40plusMatrimony*<\/span>~View <span class=font-weight-bold>  40 + 40 verified mobile numbers<\/span> of members from both the domains*~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~handpicksicon","PKGPHONECOUNT":"40","PKGSMSCOUNT":"30"},{"PKGID":"288","PKGNAME":"Combo","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"14300","PKGDISCOUNTEDRATE":"9200","PKGRATE":"5100","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with members on both <span class=font-weight-bold>MbobileShop<\/span> and <span class=font-weight-bold>40plusMatrimony*<\/span>~View <span class=font-weight-bold>  75 + 75 verified mobile numbers<\/span> of members from both the domains*~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~handpicksicon","PKGPHONECOUNT":"75","PKGSMSCOUNT":"60"},{"PKGID":"675","PKGNAME":"Gold Combo Till U Marry","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"23900","PKGDISCOUNTEDRATE":"16900","PKGRATE":"7000","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages,chat<\/span> with members on both <span class=font-weight-bold>MbobileShop<\/span> and <span class=font-weight-bold>40plusMatrimony*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> Unlimited Mobile Numbers*<\/span> <div style=display:inline-block;><div style=display:none; class=UNLIMITED_CONTACT_NO_BENEFITS_POPUP675><div class=benefits-prime-tooltip><span class=benefits-info-close onclick=closePrimeBenefitsInfo(675)><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/images\/close-icon-black.svg \/><\/span><div class=benefits-info-list><span class=benefits-info-title d-block>View unlimited phone numbers of the accepted prospects<\/span><\/div><\/div><div class=white-overlay-prime><\/div><\/div><\/div><span onclick=openPrimeBenefitsInfo(675) class=benefits-info-icon><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/revamp-images\/tool-tip-icon.svg style=vertical-align:middle;cursor:pointer;> <\/span>~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~handpicksicon","PKGPHONECOUNT":"80","PKGSMSCOUNT":""},{"PKGID":"327","PKGNAME":"PRIME Gold","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"7500","PKGDISCOUNTEDRATE":"4400","PKGRATE":"3100","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Explore <span class=font-weight-bold>ID verified Prime & regular matches with photos,<\/span> send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold>  unlimited verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~highlightericon","PKGPHONECOUNT":"75","PKGSMSCOUNT":""},{"PKGID":"328","PKGNAME":"PRIME Gold","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"13500","PKGDISCOUNTEDRATE":"9000","PKGRATE":"4500","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Explore <span class=font-weight-bold>ID verified Prime & regular matches with photos,<\/span> send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold>  unlimited verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~highlightericon","PKGPHONECOUNT":"150","PKGSMSCOUNT":""},{"PKGID":"443","PKGNAME":"PRIME Platinum","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"9500","PKGDISCOUNTEDRATE":"4300","PKGRATE":"5200","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Explore <span class=font-weight-bold>ID verified Prime & regular matches with photos,<\/span> send <span class=font-weight-bold>unlimited messages & chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> unlimited verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing<span class=font-weight-bold> unlimited horoscopes<\/span>~Get <span class=font-weight-bold>better visibility and responses<\/span> from matches with 1-month Profile Highlighter","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~highlightericon","PKGPHONECOUNT":"150","PKGSMSCOUNT":""},{"PKGID":"444","PKGNAME":"PRIME Platinum","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"17100","PKGDISCOUNTEDRATE":"8900","PKGRATE":"8200","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Explore <span class=font-weight-bold>ID verified Prime & regular matches with photos,<\/span> send <span class=font-weight-bold>unlimited messages & chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> unlimited verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing<span class=font-weight-bold> unlimited horoscopes<\/span>~Get <span class=font-weight-bold>better visibility and responses<\/span> from matches with 3-month Profile Highlighter","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~highlightericon","PKGPHONECOUNT":"300","PKGSMSCOUNT":""},{"PKGID":"599","PKGNAME":"Assisted PRIME","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"26900","PKGDISCOUNTEDRATE":"4000","PKGRATE":"22900","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span>~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"40","PKGSMSCOUNT":""},{"PKGID":"600","PKGNAME":"Assisted PRIME","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"48400","PKGDISCOUNTEDRATE":"7300","PKGRATE":"41100","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span>~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"75","PKGSMSCOUNT":""},{"PKGID":"601","PKGNAME":"Assisted PRIME","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"80700","PKGDISCOUNTEDRATE":"12100","PKGRATE":"68600","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span>~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"115","PKGSMSCOUNT":""},{"PKGID":"674","PKGNAME":"Prime Till U Marry","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"22500","PKGDISCOUNTEDRATE":"15400","PKGRATE":"7100","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Explore <span class=font-weight-bold>ID verified Prime & regular matches with photos,<\/span> send <span class=font-weight-bold>unlimited messages <\/span>&<span class=font-weight-bold> chat*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold>  unlimited verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with matches by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~payprimerelationship~highlightericon","PKGPHONECOUNT":"140","PKGSMSCOUNT":""},{"PKGID":"361","PKGNAME":"Assisted Supreme","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"42000","PKGDISCOUNTEDRATE":"2100","PKGRATE":"39900","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated Sr. Relationship manager~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package~Chance to be part of our exclusive Elite database**~<span class=font-weight-bold>FREE<\/span> Astro Match included","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon~freeaddonicon~exclusiveeliteicon","PKGPHONECOUNT":"40","PKGSMSCOUNT":""},{"PKGID":"362","PKGNAME":"Assisted Supreme","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"55000","PKGDISCOUNTEDRATE":"2800","PKGRATE":"52200","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated Sr. Relationship manager~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package~Chance to be part of our exclusive Elite database**~<span class=font-weight-bold>FREE<\/span> Astro Match included","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon~freeaddonicon~exclusiveeliteicon","PKGPHONECOUNT":"75","PKGSMSCOUNT":""},{"PKGID":"363","PKGNAME":"Assisted Supreme","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"95000","PKGDISCOUNTEDRATE":"5100","PKGRATE":"89900","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Dedicated Sr. Relationship manager~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All the benefits of Prime Gold package~Chance to be part of our exclusive Elite database**~<span class=font-weight-bold>FREE<\/span> Astro Match included","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon~freeaddonicon~exclusiveeliteicon","PKGPHONECOUNT":"115","PKGSMSCOUNT":""},{"PKGID":"433","PKGNAME":"PRIME Combo","PKGDURATION":"90","PKGEXTRADURATION":"0","PKGACTUALRATE":"11300","PKGDISCOUNTEDRATE":"7100","PKGRATE":"4200","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with <span class=font-weight-bold>ID verified Prime<\/span> and regular members on both <span class=font-weight-bold>MbobileShop<\/span> & <span class=font-weight-bold>40plusMatrimony*<\/span>~View <span class=font-weight-bold> unlimited verified mobile numbers<\/span> of members from both the domains*~An exclusive <span class=font-weight-bold>Prime Relationship team<\/span> to assist you~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~payprimerelationship~highlightericon","PKGPHONECOUNT":"55","PKGSMSCOUNT":""},{"PKGID":"434","PKGNAME":"PRIME Combo","PKGDURATION":"180","PKGEXTRADURATION":"0","PKGACTUALRATE":"20300","PKGDISCOUNTEDRATE":"13500","PKGRATE":"6800","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with <span class=font-weight-bold>ID verified Prime<\/span> and regular members on both <span class=font-weight-bold>MbobileShop<\/span> & <span class=font-weight-bold>40plusMatrimony*<\/span>~View <span class=font-weight-bold> unlimited verified mobile numbers<\/span> of members from both the domains*~An exclusive <span class=font-weight-bold>Prime Relationship team<\/span> to assist you~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>~Get <span class=font-weight-bold>better visibility and responses<\/span> from matches with 1-month Profile Highlighter","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon~payprimerelationship~highlightericon","PKGPHONECOUNT":"115","PKGSMSCOUNT":""},{"PKGID":"435","PKGNAME":"PRIME Combo","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"33800","PKGDISCOUNTEDRATE":"","PKGRATE":"33800","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with <span class=font-weight-bold>ID verified Prime<\/span> and regular members on both <span class=font-weight-bold>MbobileShop<\/span> & <span class=font-weight-bold>40plusMatrimony*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> 170 verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~payprimerelationship~highlightericon","PKGPHONECOUNT":"170","PKGSMSCOUNT":""},{"PKGID":"676","PKGNAME":"Prime Combo Till U Marry","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"33800","PKGDISCOUNTEDRATE":"24200","PKGRATE":"9600","PKGFEATURE":"","PKGTYPE":"prime","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages, chat<\/span> with <span class=font-weight-bold>ID verified Prime<\/span> and regular members on both <span class=font-weight-bold>MbobileShop<\/span> & <span class=font-weight-bold>40plusMatrimony*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> Unlimited Mobile Numbers*<\/span> <div style=display:inline-block;><div style=display:none; class=UNLIMITED_CONTACT_NO_BENEFITS_POPUP676><div class=benefits-prime-tooltip><span class=benefits-info-close onclick=closePrimeBenefitsInfo(676)><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/images\/close-icon-black.svg \/><\/span><div class=benefits-info-list><span class=benefits-info-title d-block>View unlimited phone numbers of the accepted prospects<\/span><\/div><\/div><div class=white-overlay-prime><\/div><\/div><\/div><span onclick=openPrimeBenefitsInfo(676) class=benefits-info-icon><img src=https:\/\/imgs.MbobileShop.com\/webapp-assets\/revamp-images\/tool-tip-icon.svg style=vertical-align:middle;cursor:pointer;> <\/span>~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"relationshipicon~phoneicon~horoscopeicon~payprimerelationship~highlightericon","PKGPHONECOUNT":"110","PKGSMSCOUNT":""},{"PKGID":"306","PKGNAME":"Assisted Gold","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"74700","PKGDISCOUNTEDRATE":"9000","PKGRATE":"65700","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Dedicated <span class=font-weight-bold>Relationship manager<\/span> shortlists, connects with relevant matches and arranges meetings~Get <span class=font-weight-bold>more matches<\/span> across Matrimony.com group of sites~Get more responses as even <span class=font-weight-bold>Free members can send you messages<\/span>~All benefits of Gold Package","PKGBENIFITIMG":"payprimerelationship~handpicksicon~moremessageicon~premiumcrownicon","PKGPHONECOUNT":"75","PKGSMSCOUNT":"60"},{"PKGID":"439","PKGNAME":"Combo","PKGDURATION":"365","PKGEXTRADURATION":"0","PKGACTUALRATE":"23900","PKGDISCOUNTEDRATE":"","PKGRATE":"23900","PKGFEATURE":"","PKGTYPE":"regular","PKGBENIFIT":"Send <span class=font-weight-bold>unlimited messages,chat<\/span> with members on both <span class=font-weight-bold>MbobileShop<\/span> and <span class=font-weight-bold>40plusMatrimony*<\/span>~Connect with your preferred matches, view<span class=font-weight-bold> 115 verified mobile numbers*<\/span>~Check <span class=font-weight-bold>compatibility<\/span> with preferred matches on both domains by viewing <span class=font-weight-bold>unlimited horoscopes<\/span>","PKGBENIFITIMG":"chaticon~phoneicon~horoscopeicon","PKGPHONECOUNT":"115","PKGSMSCOUNT":""}],"PAYNOWBUTTONTRACKNO":"262"},"CITRUSPAY":"","ADDONPKGINFO":{"PKG":[{"PKGID":"277","PKGNAME":"Profile Highlighter","PKGDURATION":"20","PKGACTUALRATE":"350","PKGDISCOUNTEDRATE":"Rs. 350","PKGRATE":"350"}]},"GAMOOGAPOPUPFLAG":"1","COMMUNITYDOMAINNAME":"Community","IS_MONEYBACK_AVAILABLE":"1","MEMBERSHIP_EXPIRES_IN":"0"}';
    var offerEndDate = '2025-07-31 05:59:59';
    var response = jQuery.parseJSON(jsonresponse);
    var SUCCESS_STORIES = response['SUCCESS_STORIES']['SUCCESSSTORIESNAMES'].split('~');
    var BenefitsIcons = jQuery.parseJSON(Benefitsiconjson);
    var PackageBenefitsArray = response['PKGINFO']['PKG'];
    var Category = 0;
    /*::::::::::::::::::::::::::::::::Variable Initalization ::::::::::::::::::::::::::::::::::::*/
    function paymentTypeDet(selectPack = '') {
      var OLDPAYMENTSCREEN = 0;
      var EPRPAYMENTPAGE = response['EPRPAYMENTPAGE']['FLAG'];
      var SIMPLIFIEDPAGE = response['SIMPLIFIEDPAGE']['FLAG'];
      OLDPAYMENTSCREEN = '1';
      var BACKTOSCREEN = '';
      var freebieoffertext = 'Get a flat Rs.3100 on 3 month Gold Pack';
      //EPRPAYMENTPAGE = 0;
      if (EPRPAYMENTPAGE == 1 && OLDPAYMENTSCREEN == '') {
        var PACKIDDET = response['EPRPAYMENTPAGE']['PKG']['PKGID'];
        var PACKBENEFITDETS = response['EPRPAYMENTPAGE']['PKG']['PKGBENIFIT'];
        var PACKBENEFITDETSDET = PACKBENEFITDETS.split('~');
        console.log('PACKIDDET == ' + PACKBENEFITDETSDET);
        document.getElementById("eprpayment").style.display = "block";
        document.getElementById("simplifypayment").style.display = "none";
        document.getElementById("packages-center-section").style.display = "none";
        if (freebieoffertext != '') {
          document.getElementById("packages-center-section1").style.display = "none";
        }
        var offerHeading = "<div class='simplify-payment-title'>Become a paid member to contact matches<\/div>";
        let restrictbenefitarr = ['1', '2', '436', '327', '328', '329', '673', '674'];	
        if (restrictbenefitarr.includes(PACKIDDET)) {
          // var ANEXCLUSIVE = PACKBENEFITDETSDET[3].replace("@#@", "");
          document.getElementById("packbenefitdetepr").innerHTML = '<div class="sunday-offer-list"><ul>' + offerHeading + '<li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li></ul></div>';
        } else if (PACKIDDET == 361 || PACKIDDET == 362 || PACKIDDET == 363) {
          document.getElementById("packbenefitdetepr").innerHTML = '<div class="sunday-offer-list"><ul>' + offerHeading + '<li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li><li><span>' + PACKBENEFITDETSDET[3] + '</span></li><li><span>' + PACKBENEFITDETSDET[4] + '</span></li><li><span>' + PACKBENEFITDETSDET[5] + '</span></li></ul></div>';
        } else {
          document.getElementById("packbenefitdetepr").innerHTML = '<div class="sunday-offer-list"><ul>' + offerHeading + '<li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li><li><span>' + PACKBENEFITDETSDET[3] + '</span></li></ul></div>';
        }
        document.getElementById("simplifychat").innerHTML = '<div class="paytopqueries">' +
            '<span style="margin-right: 20px;font-size: 10px;letter-spacing: 0.30px;">Need help in making payment?</span> ' +
            '<span onClick="ChatWithUS(1);" style="cursor: pointer;">' +
            '<img src="https://imgs.MbobileShop.com/bmimgs/payments/chat-icon.svg" width="14" height="16" style="vertical-align: middle;margin-right: 4px;">Chat with us</span>' +
                          ''
                      '</div>';

        document.getElementById("simplyfyurl").value = PACKIDDET;
      } else if (EPRPAYMENTPAGE == 0 && SIMPLIFIEDPAGE == 1 && OLDPAYMENTSCREEN == '') {
        var ADDONOFFERPKGINFO = response['ADDONOFFERPKGINFO'];
        var SADDONOFFERPKGINFO = ADDONOFFERPKGINFO.split('~');
        var PACKBENEFITDETS = response['SIMPLIFIEDPAGE']['PKG'][0]['PKGBENIFIT'];
        document.getElementById("eprpayment").style.display = "none";
        document.getElementById("simplifypayment").style.display = "block";
        document.getElementById("packages-center-section").style.display = "none";
        if (freebieoffertext != '') {
          document.getElementById("packages-center-section1").style.display = "none";
        }
        document.getElementById("simplifychat").innerHTML = '<div class="paytopqueries">' +
            '<span style="margin-right: 20px;font-size: 10px;letter-spacing: 0.30px;">Need help in making payment?</span> ' +
            '<span onClick="ChatWithUS(1);" style="cursor: pointer;">' +
            '<img src="https://imgs.MbobileShop.com/bmimgs/payments/chat-icon.svg" width="14" height="16" style="vertical-align: middle;margin-right: 4px;">Chat with us</span>' +
                          ''
                      '</div>';

        if (BACKTOSCREEN != '' && selectPack == '') {
          SADDONOFFERPKGINFO[0] = BACKTOSCREEN;
        } else {
          if (selectPack == '') {
            SADDONOFFERPKGINFO[0] = SADDONOFFERPKGINFO[0];
          } else {
            SADDONOFFERPKGINFO[0] = selectPack;
          }
        }
        if (SADDONOFFERPKGINFO[0] == 1) {
          var PACKBENEFITDETS = response['SIMPLIFIEDPAGE']['PKG'][0]['PKGBENIFIT'];
          var PACKBENEFITDETSDET = PACKBENEFITDETS.split('~');
          var ANEXCLUSIVE = PACKBENEFITDETSDET[2].replace("@#@", "");
          var ANEXCLUSIVE1 = PACKBENEFITDETSDET[3].replace("@#@", "");
          var ANEXCLUSIVE2 = PACKBENEFITDETSDET[4].replace("@#@", "");
          document.getElementById("goldpack1").classList.add("active-radio-box");
          document.getElementById("goldpack").checked = true;
          document.getElementById("primegoldpack1").classList.remove("active-radio-box");
          document.getElementById("primegoldpack").checked = false;
          document.getElementById('primeplatinumpack1').classList.remove("active-radio-box");
          document.getElementById('primeplatinumpack').checked = false;
          document.getElementById("packpricedet").innerHTML = '2,200';
          document.getElementById("activePlan_period").innerHTML = '2,200';
          document.getElementById("activePlan_element").innerHTML = "GOLD";
          document.getElementById("activePlanMonth_element").innerHTML = "3 months";
          document.getElementById("simplyfyurl").value = SADDONOFFERPKGINFO[0];
          document.getElementById("packbenefitdet").innerHTML = '<div class="sunday-offer-list"><ul><li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li class="cross-tick"><span class="cross-tick1">' + ANEXCLUSIVE + '</span></li></ul></div>';
          //<li  class="cross-tick"><span class="cross-tick1">' + ANEXCLUSIVE1 + '</span></li><li  class="cross-tick"><span class="cross-tick1">' + ANEXCLUSIVE2 + '</span></li>
        } else if (SADDONOFFERPKGINFO[0] == 327) {
          var PACKBENEFITDETS = response['SIMPLIFIEDPAGE']['PKG'][1]['PKGBENIFIT'];
          var PACKBENEFITDETSDET = PACKBENEFITDETS.split('~');
          var ANEXCLUSIVE = PACKBENEFITDETSDET[3].replace("@#@", "");
          var ANEXCLUSIVE2 = PACKBENEFITDETSDET[4].replace("@#@", "");
          document.getElementById("goldpack1").classList.remove("active-radio-box");
          document.getElementById("goldpack").checked = false;
          document.getElementById("primegoldpack1").classList.add("active-radio-box");
          document.getElementById("primegoldpack").checked = true;
          document.getElementById('primeplatinumpack1').classList.remove("active-radio-box");
          document.getElementById('primeplatinumpack').checked = false;
          document.getElementById("packpricedet").innerHTML = '3,100';
          document.getElementById("activePlan_period").innerHTML = '3,100';
          document.getElementById("activePlan_element").innerHTML = "PRIME GOLD";
          document.getElementById("activePlanMonth_element").innerHTML = "3 months";
          document.getElementById("simplyfyurl").value = SADDONOFFERPKGINFO[0];
          document.getElementById("packbenefitdet").innerHTML = '<div class="sunday-offer-list"><ul><li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li></ul></div>';

          //<li><span>' + ANEXCLUSIVE + '</span></li><li class="cross-tick"><span class="cross-tick1">' + ANEXCLUSIVE2 + '</span></li>
        } else if (SADDONOFFERPKGINFO[0] == 328) {
          var PACKBENEFITDETS = response['SIMPLIFIEDPAGE']['PKG'][2]['PKGBENIFIT'];
          var PACKBENEFITDETSDET = PACKBENEFITDETS.split('~');
          document.getElementById("goldpack1").classList.remove("active-radio-box");
          document.getElementById("goldpack").checked = false;
          document.getElementById("primegoldpack1").classList.remove("active-radio-box");
          document.getElementById("primegoldpack").checked = false;
          document.getElementById('primeplatinumpack1').classList.add("active-radio-box");
          document.getElementById('primeplatinumpack').checked = true;
          document.getElementById("packpricedet").innerHTML = '7,100';
          document.getElementById("activePlan_period").innerHTML = '7,100';
          document.getElementById("activePlan_element").innerHTML = "PRIME GOLD";
          document.getElementById("activePlanMonth_element").innerHTML = "6 months";
          document.getElementById("simplyfyurl").value = SADDONOFFERPKGINFO[0];
          document.getElementById("packbenefitdet").innerHTML = '<div class="sunday-offer-list"><ul><li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li><li><span>' + PACKBENEFITDETSDET[3] + '</span></li></ul></div>';
        }else if (SADDONOFFERPKGINFO[0] == 674) {
          var PACKBENEFITDETS = response['SIMPLIFIEDPAGE']['PKG'][2]['PKGBENIFIT'];
          var PACKBENEFITDETSDET = PACKBENEFITDETS.split('~');
          var ANEXCLUSIVE = PACKBENEFITDETSDET[3].replace("@#@", "");
          var ANEXCLUSIVE2 = PACKBENEFITDETSDET[4].replace("@#@", "");
          document.getElementById("goldpack1").classList.remove("active-radio-box");
          document.getElementById("goldpack").checked = false;
          document.getElementById("primegoldpack1").classList.remove("active-radio-box");
          document.getElementById("primegoldpack").checked = false;
          document.getElementById('primeplatinumpack1').classList.add("active-radio-box");
          document.getElementById('primeplatinumpack').checked = true;
          document.getElementById("packpricedet").innerHTML = '7,100';
          document.getElementById("activePlan_period").innerHTML = '7,100';
          document.getElementById("activePlan_element").innerHTML = "PRIME - Till U Marry";
          document.getElementById("activePlanMonth_element").innerHTML = '';
          document.getElementById("simplyfyurl").value = SADDONOFFERPKGINFO[0];
          document.getElementById("packbenefitdet").innerHTML = '<div class="sunday-offer-list"><ul><li><span>' + PACKBENEFITDETSDET[0] + '</span></li><li><span>' + PACKBENEFITDETSDET[1] + '</span></li><li><span>' + PACKBENEFITDETSDET[2] + '</span></li></ul></div>';

          //<li><span>' + ANEXCLUSIVE + '</span></li>
        }
      } else {
        document.getElementById("eprpayment").style.display = "none";
        document.getElementById("simplifypayment").style.display = "none";
        document.getElementById("packages-center-section").style.display = "block";

        document.getElementById("simplifychat").innerHTML = '<div class="paytopqueries">' +

                      ''
                  '</div>';


        document.getElementById("activePlan_period").innerHTML = '2,200';
        document.getElementById("activePlan_element").innerHTML = "GOLD";
        document.getElementById("activePlanMonth_element").innerHTML = "3 months";
        if (freebieoffertext != '') {
          document.getElementById("packages-center-section1").style.display = "block";
        }
      }
    }

    function getRedirectURl() {
      var packIdDet = document.getElementById("simplyfyurl").value;
      var packURL = "https://mbobileshop.com/payments/paymentmode.php?category=" + packIdDet + "&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&APPTYPE=300&encip=&PAYMENTOPT=&ip=&Id=SDE0NTUwNTQ3";
      window.location.href = packURL;
    }

    function CallUs(calDet) {
      if (calDet == 1) {
        ajaxpayment('CALLUS');
      }
    }
    //****************************************Simplfy Payment Complete*********************************************************/
    /*::::::::::::::::::::::::::::::::Success Stories ::::::::::::::::::::::::::::::::::::*/
    if (SUCCESS_STORIES.length > 3) {
      $('.success-swiper-button-next').css("display", "block");
      $('.success-swiper-button-prev').css("display", "block");
      var swiper = new Swiper('.s2', {
        slidesPerView: 3, //swipe 1 by one
        spaceBetween: 0,
        navigation: {
          nextEl: '.success-swiper-button-next',
          prevEl: '.success-swiper-button-prev',
        },
      });
    } else {
      $('.success-swiper-button-next').css("display", "none");
      $('.success-swiper-button-prev').css("display", "none");
    }
    /*::::::::::::::::::::::::::::::::Success Stories ::::::::::::::::::::::::::::::::::::*/
    /*::::::::::::::::::::::::::::::::Package Selection ::::::::::::::::::::::::::::::::::::*/
              var ADDONOFFERPKGINFO = response['ADDONOFFERPKGINFO'];
      if (ADDONOFFERPKGINFO != '' && ADDONOFFERPKGINFO != undefined && ADDONOFFERPKGINFO != null) {
        var SADDONOFFERPKGINFO = ADDONOFFERPKGINFO.split('~');
        Category = SADDONOFFERPKGINFO[0];
      }
        PackageDisplay(Category);
    /*::::::::::::::::::::::::::::::::Package Selection ::::::::::::::::::::::::::::::::::::*/
    /*::::::::::::::::::::::::::::::::Best Seller Selection ::::::::::::::::::::::::::::::::::::*/
    function BestSeller() {
      var target = $('.package-duration');
      var membershiptype = $('.membershipselected').attr("data-type");
      $('html,body').animate({
        scrollTop: target.offset().top
      }, "slow");
      //var PKGBESTSELLER='';
      if (membershiptype == 'prime') {
        var PKGBESTSELLER = '327';
      } else {
        var PKGBESTSELLER = '1';
      }
      var PKGMSTPPLR = '4';
      if (PKGBESTSELLER == '' || PKGBESTSELLER == undefined || PKGBESTSELLER == null && PKGMSTPPLR != '') {
        PKGBESTSELLER = PKGMSTPPLR;
      }
      if (PKGBESTSELLER == '' || PKGBESTSELLER == undefined || PKGBESTSELLER == null) {
        PackageDisplay(3);
      } else {
        var PKGBEST = package_type_array[PKGBESTSELLER];
        var BestMonthly = MonthlyBasedArray[PKGBEST];
        changePackage(BestMonthly, PKGBESTSELLER);
        _gaq.push(['_trackEvent', PageType, 'BUTTON', 'BESTSELLER-TAB']);
        ajaxpayment('BESTSELLER-TAB', BestMonthly);
      }
    }
    /*::::::::::::::::::::::::::::::::Best Seller Selection ::::::::::::::::::::::::::::::::::::*/
    /*::::::::::::::::::::::::::::::::Assisted Package Selection ::::::::::::::::::::::::::::::::::::*/
    function AssistedPackage(PackageID) {
      var target = $('.package-duration');
      $('html,body').animate({
        scrollTop: target.offset().top
      }, "slow");
      var package_type = package_type_array[PackageID];
      var Monthly = MonthlyBasedArray[package_type];
      changePackage(Monthly, PackageID);
      var Assited_package_type_array = {
        48: 'ASSISTED3-TAB',
        80: 'ASSISTED6-TAB',
        306: 'ASSISTED12-TAB',
        361: 'ASSISTEDS3-TAB',
        362: 'ASSISTEDS6-TAB',
        363: 'ASSISTEDS12-TAB'
      }
      _gaq.push(['_trackEvent', PageType, 'BUTTON', Assited_package_type_array[PackageID]]);
      ajaxpayment(Assited_package_type_array[PackageID], Monthly);
    }
    /*::::::::::::::::::::::::::::::::Assisted Package Selection ::::::::::::::::::::::::::::::::::::*/
    /*::::::::::::::::::::::::::::::::Become Premium ::::::::::::::::::::::::::::::::::::*/
    function BecomePremium($type = 1) {
      var target = $('.package-duration');
      var membershiptype = $('.membershipselected').attr("data-type");
      $('html,body').animate({
        scrollTop: target.offset().top
      }, "slow");
      var buttontype = '';
      if ($type == 1) buttontype = 'PREMIUM-MEMBER-TAB';
      if ($type == 2) buttontype = 'MEMBERSHIP-PACKAGE-TAB';
      var PKGMSTPPLR = '4';
      if (membershiptype == 'prime') {
        var PKGBESTSELLER = '327';
      } else {
        var PKGBESTSELLER = PKGMSTPPLR;
      }
      var PKGBEST = package_type_array[PKGBESTSELLER];
      var BestMonthly = MonthlyBasedArray[PKGBEST];
      changePackage(BestMonthly, PKGBESTSELLER);
      _gaq.push(['_trackEvent', PageType, 'BUTTON', buttontype]);
      ajaxpayment(buttontype, '');
      //PackageDisplay();	
    }
    /*::::::::::::::::::::::::::::::::Become Premium ::::::::::::::::::::::::::::::::::::*/
    /*::::::::::::::::::::::::::::::::Membership Packages::::::::::::::::::::::::::::::::::::*/
    function PackageDisplay(Category = '', membershiptype = '') {
      if (Category == '') {
                  membershiptype = 'prime';
                changePackage(3, '', membershiptype);
      } else {
        var package_type = package_type_array[Category];
        var Monthly = MonthlyBasedArray[package_type];
        membershiptype = 'regular';
                  var Prime_package_array = response['PRIME_PACKAGE'];
          if (Category) {
            if (jQuery.inArray(Category, Prime_package_array) !== -1)
              membershiptype = 'prime';
          }
                if (Monthly != '' && Monthly != undefined)
          changePackage(Monthly, Category, membershiptype);
        else
          changePackage(3, '', membershiptype);
      }
    }
    /*::::::::::::::::::::::::::::::::Membership Packages::::::::::::::::::::::::::::::::::::*/
    $(".membership_package").click(function() {
      $(".membership_package").removeClass('tab_underline');
      $(".membership_package").removeClass('membershipselected');
      $(this).addClass("tab_underline");
      $(this).addClass("membershipselected");
      changePackage(3, '', $(this).attr("data-type"));
      var TABtype = '';
      if ($(this).attr("data-type") == 'regular') TABtype = 'REGULAR-TAB';
      else TABtype = 'PRIME-TAB';
      _gaq.push(['_trackEvent', PageType, 'TAB', TABtype]);
      ajaxpayment(TABtype, '');
    });
    $(".tablinks").click(function() {
      var packagemonth = $(this).attr("idval");
      var TABtype = '';
      if (packagemonth == 3) TABtype = '3MNTHS-TAB';
      if (packagemonth == 6) TABtype = '6MNTHS-TAB';
      if (packagemonth == 12) TABtype = '12MNTHS-TAB';
      if (packagemonth == 'tum') TABtype = 'TUM-TAB';
      _gaq.push(['_trackEvent', PageType, 'TAB', TABtype]);
      ajaxpayment(TABtype, '');
      membershiptype = $('.membershipselected').attr("data-type");
      changePackage(packagemonth, '', membershiptype);
    });
    /*::::::::::::::::::::::::::::::::Dynamic Membership Packages::::::::::::::::::::::::::::::::::::*/
    var myswiper;

    function changePackage(month, Package = '', membershiptype = '') {
      if (membershiptype == '') {
        membershiptype = $('.membershipselected').attr("data-type")
                  var Prime_package_array = response['PRIME_PACKAGE'];
          Package = Package.toString();
          if (Package != '') {
            membershiptype = 'regular';
            if (jQuery.inArray(Package, Prime_package_array) !== -1)
              membershiptype = 'prime';
          }
              }
      if ($('.membershipselected').attr("data-type") == 'prime') {
        $('#AssistedSupreme').css("display", "block");
        $('#AssistedServiceSection').css("display", "none");
      } else {
        $('#AssistedSupreme').css("display", "none");
        $('#AssistedServiceSection').css("display", "block");
      }
      $('.membership_package').removeClass("tab_underline");
      $('.membership_package').removeClass("membershipselected");
      if (membershiptype == 'regular') {
        $('#regularpackage').addClass("tab_underline");
        $('#regularpackage').addClass("membershipselected");
        // START MATRIMONY-319
        $("#package-prime-banner").hide();
        $("#AssistedSupreme").hide();
        $(".prime_eligible_terms_and_conditions").hide();
        $(".assprime_eligible_terms_and_conditions").hide();
        $(".regular_eligible_terms_and_conditions").show();
        $("#prime_tooltip").show();
        // END MATRIMONY-319
      } else {
        $('#primepackage').addClass("tab_underline");
        $('#primepackage').addClass("membershipselected");
        $('#AssistedServiceSection').css("display", "none");
        // START MATRIMONY-319
        $("#package-prime-banner").show();
        $("#AssistedSupreme").show();
        $(".prime_eligible_terms_and_conditions").show();
        $(".assprime_eligible_terms_and_conditions").show();
        $(".regular_eligible_terms_and_conditions").hide();
        $("#prime_tooltip").hide();
        // END MATRIMONY-319
      }
      //:::::::::::::::REGULAR TAB::::::::::::::::::::::::::::::::::::::::::::::::::://
      if (response['PRIME_ENABLE'] == 1 && response['TWINPRIME_ENABLE'] == 0 && membershiptype == 'prime') {
        $('.regulartab').css("display", "block");
        $(".tablinks").each(function(index, element) {
          if (element.id == month + 'month') {
            $('#' + $(element).attr("idval") + 'label').removeClass('inactivelabel');
            $('#' + $(element).attr("idval") + 'label').addClass('update-chip-label');
            $('#' + element.id).removeClass('update-chip-inactive');
            $('#' + element.id).addClass('update-chip-active');
          } else {
            $('#' + $(element).attr("idval") + 'label').removeClass('update-chip-label');
            $('#' + $(element).attr("idval") + 'label').addClass('inactivelabel');
            $('#' + element.id).removeClass('update-chip-active');
            $('#' + element.id).addClass('update-chip-inactive');
          }
        });
      } else {
        $('.regulartab').css("display", "block");
        $(".tablinks").each(function(index, element) {
          if (element.id == month + 'month') {
            $('#' + $(element).attr("idval") + 'label').removeClass('inactivelabel');
            $('#' + $(element).attr("idval") + 'label').addClass('update-chip-label');
            $('#' + element.id).removeClass('update-chip-inactive');
            $('#' + element.id).addClass('update-chip-active');
          } else {
            $('#' + $(element).attr("idval") + 'label').removeClass('update-chip-label');
            $('#' + $(element).attr("idval") + 'label').addClass('inactivelabel');
            $('#' + element.id).removeClass('update-chip-active');
            $('#' + element.id).addClass('update-chip-inactive');
          }
        });
      }
      //:::::::::::::::REGULAR TAB::::::::::::::::::::::::::::::::::::::::::::::::::://
      //:::::::::::::::::::::::::::Package Benefits ::::::::::::::::::::::::::::::://
      if (PackageBenefitsArray) {
        var PackageBenefitHtml = '';
        var PackageTotal = 0;
        var PackagePosition = 0;
        $.each(PackageBenefitsArray, function(key, data) {
          var MonthlyCheck = 1;
          var PackageCheck = 1;
          var Packageclass = "";
                      if (data['PKGTYPE'] != membershiptype) {
              PackageCheck = 0;
            }
                    if (membershiptype == 'regular') {
            // if (data['PKGDURATION'] != MonthArray[month]) MonthlyCheck = 0;
            if (!MonthArrayPkg[month].includes(data['PKGID'])) MonthlyCheck = 0;
          } else {
                        if (PackageCheck == 1) {
              // if (data['PKGDURATION'] != MonthArray[month]) MonthlyCheck = 0;
              if (!MonthArrayPkg[month].includes(data['PKGID'])) MonthlyCheck = 0;
            }
                      }
          //if(data['PKGDURATION']==270) MonthlyCheck=0;
          if (MonthlyCheck == 1 && data['PKGNAME'] != '' && data['PKGBENIFIT'] != '' && data['PKGBENIFITIMG'] != '' && PackageCheck == 1) {
            PackageTotal++;
            if (Package != '') {
              if (Package == data['PKGID']) {
                PackagePosition = PackageTotal;
                Packageclass = "package-selected";
              }
            }
            PackageBenefitHtml += '<div class="swiper-slide package-swiper-slide payment-info-box ' + Packageclass + ' " attr-package-id="' + data['PKGID'] + '" id="' + data['PKGID'] + 'div">';
            //Recommended
            if (response['PKGRECOMMENDED'] == data['PKGID'])
              PackageBenefitHtml += '<div class="payment-tag-img"><img src="https://imgs.MbobileShop.com/bmimgs/payments/recommended-icon.png?v=1" width="99" height="15" border="0" alt="Recommended"></div>';
            //BestSeller
            if (response['PKGBESTSELLER'] == data['PKGID'])
              PackageBenefitHtml += '<div class="payment-tag-img"><img src="https://imgs.MbobileShop.com/bmimgs/payments/bestseller-icon.png?v=1" width="82" height="15" border="0" alt="Best Seller"></div>';
            //PKGBESTVALUEFORMONEY
            if (response['PKGBESTVALUEFORMONEY'] == data['PKGID'])
              PackageBenefitHtml += '<div class="payment-tag-img"><img src="https://imgs.MbobileShop.com/bmimgs/payments/best-value-money.png?v=1" width="130" height="15" border="0" alt="Best Value For Money"></div>';
            //PKGMOSTPOPULAR
            if (response['PKGMOSTPOPULAR'] == data['PKGID'])
              PackageBenefitHtml += '<div class="payment-tag-img"><img src="https://imgs.MbobileShop.com/bmimgs/payments/pay-most-popular.svg?v=1" width="" height="" border="0" alt="Most Popular"></div>';
            //PKGMOSTPOPULAR
            if (response['PRIMEPKGMOSTPOPULAR'] == data['PKGID'])
              PackageBenefitHtml += '<div class="payment-tag-img"><img src="https://imgs.MbobileShop.com/bmimgs/payments/bestseller-icon.png?v=1"  width="82" height="15" border="0" alt="Most Popular"></div>';
            PackageBenefitHtml += '<div style="padding:16px;font-size:14px;">';
            var packagename = data['PKGNAME'];
            if (data['PKGID'] == 237) {
              packagename = data['PKGNAME'] + ' <sup style="font-size: 10px; color:#808080">SM</sup>';
            }
            packagename = packagename.replace('Prime', 'PRIME');
            packagename = packagename.replace('TwinPack', 'Combo');
            packagename = packagename.replace('TUM', '');

            PackageBenefitHtml += '<span style="padding-bottom: 6px;font-size: 14px;font-weight: 700;line-height: 17px;display: inline-block;width: 60%;text-align: left;">' + packagename;

            if(data['PKGEXTRADURATION'] != 0){
              PackageBenefitHtml += ' + </span>';
            }else{
              PackageBenefitHtml += '</span>';
            }
            PackageBenefitHtml += '<span style="text-align: right;font-size: 14px;display: inline-block;width: 40%;vertical-align: top;">' + response['PKGCURRENCY'] + adddcomma(data['PKGACTUALRATE']) + '</span><div style="clear:both;"></div>';

            var Benefits = data['PKGBENIFIT'].split('~');
            var BenICON = data['PKGBENIFITIMG'].split('~');
            var TOTALPAY = data['PKGACTUALRATE'];
            var DiscountRate = data['PKGDISCOUNTEDRATE'];
            if (DiscountRate == '' || DiscountRate == undefined || DiscountRate == 'undefined' || DiscountRate == null)
              DiscountRate = 0;
            if (Benefits) {
              //:::::::::::::::::Benefits Text::::::::::::::::::::::::::::::::::://
              PackageBenefitHtml += '<div class="payment-list-items assisted-supreme-scroll">';
              if(data['PKGEXTRADURATION'] != 0){
                let extraDayPack = Math.floor((data['PKGEXTRADURATION'] / 30));

                PackageBenefitHtml += "<div style='padding-bottom:7px;display: block;margin-top: 0px;margin-bottom: 6px;text-align: left;position: sticky;top: 0px;background: #fff;'><b>" + extraDayPack + '</b> '+ (extraDayPack == 1 ? '<b> Month </b>' : '<b> Months </b>') + "<span style='background: linear-gradient(90deg, #1BA162 0%, #288A84 100%);font-size: 10px;padding: 3px;color: #fff;border-radius: 2px;'>FREE</span></div>";
              }
              PackageBenefitHtml += '<ul style="list-style:none;margin:0px;padding:0px;">';
              $.each(Benefits, function(bkey, beft) {
                var icon = BenICON[bkey];
                if (BenICON[bkey] != 'undefined' && BenICON[bkey] != undefined) {
                  if (BenICON[bkey].indexOf('#') != -1) {
                    var icon = BenICON[bkey].replace('#', '');
                  }
                }
                var iconcls = '';
                if (icon == 'highlightericon' || icon == 'chaticon' || icon == 'understandsicon' || icon == 'messageicon' || icon == 'benefiticon' || icon == 'handpicksicon' || icon == 'relationshipicon' || icon == 'premium' || icon == 'moremessageicon' || icon == 'premiumcrownicon') {
                  iconcls = 'class="pay-icon-pos"';
                }
                var benefiturl = "https://mbobileshop.com/images/payment-revamp/" + BenefitsIcons[icon] + ".svg?=v1";
                var extrass = "";
                var addonstatus = 0;
                var checkstatus = 0;
                if (data['PKGADDONOFFER']) addonstatus = 1;
                if (beft.indexOf('@^@') != -1) {
                  extrass = "text-decoration: line-through; color:#808080";
                  beft = beft.replace('@^@', '');
                }
                if (addonstatus == 1 && extrass != '') checkstatus = 1;
                if (checkstatus == 0)
                  PackageBenefitHtml += '<li ' + iconcls + ' style="background:url(' + benefiturl + ') no-repeat;vertical-align:middle;padding: 0px 12px 7px 35px; ' + extrass + '">' + beft + '</li>';
              });
              if (data['PKGADDONOFFER']) {
                var addonplus = "https://imgs.MbobileShop.com/bmimgs/payments/pay-add-icon.png?v=1";
                PackageBenefitHtml += '<li  style="background:url(' + addonplus + ') no-repeat;vertical-align:middle;padding: 9px 0px 5px 14px;height:24px;text-align:center;width:16px;margin:0px auto;"></li>';
              }
              PackageBenefitHtml += '</ul>';
              //:::::::::::::::::Benefits Text::::::::::::::::::::::::::::::::::://
            }
            //:::::::::::::::::::::::::::::::ADDON Package Benefits:::::::::::::::::::::::::::::::::::::://				
            if (data['PKGADDONOFFER']) {
              var addonOFFER = data['PKGADDONOFFER'].split('@^@');
              var AddOfferAmount = 0;
              var AddOfferContent = '';
              var addonOFFERS;
              if (addonOFFER) {
                if (addonOFFER.length > 2) {
                  $.each(addonOFFER, function(offerkey, Offer) {
                    var OfferRate = Offer.split('~');
                    OfferRate[2] = OfferRate[2].replace('worth', '');
                    if (offerkey > 1) {
                      AddOfferContent = $.trim(AddOfferContent) + " and others worth.";
                    } else {
                      AddOfferContent += $.trim(OfferRate[2]) + ", ";
                    }
                    AddOfferAmount = parseFloat(AddOfferAmount) + parseFloat(OfferRate[3]);
                  });
                  var addonofferstring = 'AddOnOffer~~' + AddOfferContent + '~' + AddOfferAmount;
                  addonOFFERS = {
                    addonofferstring
                  };
                } else {
                  addonOFFERS = addonOFFER;
                }
                PackageBenefitHtml += '<ul style="list-style:none;margin:0px;padding:0px;">';
                $.each(addonOFFERS, function(offerkey, Offer) {
                  var Offerc = Offer.split('~');
                  if (DiscountRate != '') {
                    DiscountRate = parseFloat(DiscountRate) + parseFloat(Offerc[3]);
                  }
                  TOTALPAY = parseFloat(TOTALPAY) + parseFloat(Offerc[3]);
                  var addonurl = "https://mbobileshop.com/images/payment-revamp/" + BenefitsIcons[Offerc[0]] + ".svg?=v1";
                  PackageBenefitHtml += '<li style="background:url(' + addonurl + ') no-repeat;vertical-align:middle;padding: 0px 0px 9px 28px;width:55%;" class="left">' + Offerc[2] + '';
                  PackageBenefitHtml += ' </li>';
                  PackageBenefitHtml += ' <li style="vertical-align:middle;padding: 0px 0px 9px 0px;width: 30%;text-align: right;" class="right">' + response['PKGCURRENCY'] + adddcomma(Offerc[3]) + '</li>';
                });
                PackageBenefitHtml += '</ul>';
              }
            }
            //:::::::::::::::::::::::::::::::ADDON Package Benefits:::::::::::::::::::::::::::::::::::::://				
            PackageBenefitHtml += '</div>';
            if (data['PKGID'] == 673 || data['PKGID'] == 674 || data['PKGID'] == 675 || data['PKGID'] == 676) {
              PackageBenefitHtml += '<div style="width: 100%;"><a href="javascript:void(0);" class="knowmore-button" onclick="know_more(' +data['PKGID']+ ',463)">Know More <img src="https://mbobileshop.com/images/payment-revamp/knw-btn-arrow.svg?=v1" style="padding-left: 6px;"></a></div>';
            }
            PackageBenefitHtml += '<div class="payment-total-portion">';
            PackageBenefitHtml += '<ul style="list-style:none;margin:0px;padding:0px;">';
            var TotalHtml = '';
            var Totalvalue = '';
            if (DiscountRate != 0 && DiscountRate != '') {
              TotalHtml = 'Total';
              Totalvalue = response['PKGCURRENCY'] + adddcomma(TOTALPAY);
            }
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 0px 28px 4px 0px;height: 17px;" class="left"><span>' + TotalHtml + '</span></li>';
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 0px 0px 4px 0px;height: 17px;" class="right"><span>' + Totalvalue + '</span></li>';
            //:::::::::::::::::::::::::::::::Discount:::::::::::::::::::::::::::::::::::::://				
            var DiscountPercentagehtml = '';
            var DiscountRatehtml = '';
            if (DiscountRate != 0 && DiscountRate != '') {
              var DiscountPercentage = Math.round(DiscountRate / parseFloat(TOTALPAY) * 100);
              TOTALPAY = parseFloat(TOTALPAY) - parseFloat(DiscountRate);
              DiscountPercentagehtml = 'Discount (' + DiscountPercentage + '%)';
              DiscountRatehtml = response['PKGCURRENCY'] + adddcomma(DiscountRate);
            }
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 0px 28px 7px 0px;color:#00a03a;font-size:14px;font-weight:700;letter-spacing: 0.42px; height: 17px;" class="left"><span>' + DiscountPercentagehtml + '</span></li>';
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 0px 0px 7px 0px;color:#00a03a;font-size:14px;font-weight:700;letter-spacing: 0.42px;height: 17px;" class="right"><span>' + DiscountRatehtml + '</span></li>';
            //:::::::::::::::::::::::::::::::Discount:::::::::::::::::::::::::::::::::::::://				
            var YouPay = 'You pay';
            if (DiscountRate != 0 && DiscountRate != '') {
              var YouPay = 'You pay';
            }
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 6px 28px 12px 0px;" class="left">' + YouPay + '</li>';
            PackageBenefitHtml += '<li style="vertical-align:middle;padding: 0px 0px 12px 0px;color:#000;font-size:20px;font-weight:900;letter-spacing: 0.6px;" class="right">' + response['PKGCURRENCY'] + adddcomma(TOTALPAY) + '';
            PackageBenefitHtml += '</li>';
            PackageBenefitHtml += '</ul>';
            PackageBenefitHtml += '</div>';
            PackageBenefitHtml += '<div style="clear:both;"></div>';
            var packagetype = package_type_array[data['PKGID']];
            var Monthly = MonthlyBasedArray[packagetype];
            var galink = '_gaq.push([\'_trackEvent\', \'' + PageType + '\', \'LINK\', \'' + packagetype + '\']);';
            var ajaxpaymentlink = 'ajaxpayment(\'' + packagetype + '\', \'' + Monthly + '\');';
            var btnclass = "btn-pay-now";
            //:::::::::::::::::::::::::::::::Pay Now:::::::::::::::::::::::::::::::::::::://				
            PackageBenefitHtml += '<div class="' + btnclass + '"><a id="' + data['PKGID'] + 'redirect" rhref="https://mbobileshop.com/payments/paymentmode.php?category=' + data['PKGID'] + '&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&APPTYPE=300&encip=&PAYMENTOPT=&ip=&Id=SDE0NTUwNTQ3" href="javascript:;" class="paynow-button">Pay Now <img src="https://mbobileshop.com/images/payment-revamp/pay-btn-arrow.svg?=v1" style="padding-left: 6px;"></a></div>';
            PackageBenefitHtml += '<div style="padding-top:6px;letter-spacing: 0.66px;line-height: 22px;color:#000;text-align:center;">';
            //:::::::::::::::::::::::::::::::Pay Now:::::::::::::::::::::::::::::::::::::://				
            //:::::::::::::::::::::::::::::::OFFERENDDATE:::::::::::::::::::::::::::::::::::::://				
            if (DiscountRate != 0 && DiscountRate != '' && offerEndDate != '') {
              PackageBenefitHtml += '<span style="font-size: 14px;">Offer valid till 31-Jul-2025';
              PackageBenefitHtml += '</span>';
            }
            //:::::::::::::::::::::::::::::::OFFERENDDATE:::::::::::::::::::::::::::::::::::::://				
            PackageBenefitHtml += '</div>';
            if (data['PKGID'] == 555) {
              PackageBenefitHtml += "<div style='position: relative;margin-top: 40px;font-size: 10px;'>" + response['ASSISTEDASSUREDPACKTERMSCONDITION'] + "</div>";
            }
            PackageBenefitHtml += '</div>';
            PackageBenefitHtml += '</div>';
          }
        });
        //if(PackageTotal>4) PackageBenefitHtml+='<div class="swiper-slide package-swiper-slide"></div>';
        if (PackageTotal < 4) {
          var newPackageBenefitHtml = '<div style="margin:0 auto;">';
          newPackageBenefitHtml += PackageBenefitHtml;
          newPackageBenefitHtml += '<div>';
          PackageBenefitHtml = newPackageBenefitHtml;
        }
        $('.package-swiper-wrapper').html(PackageBenefitHtml);
      }
      //:::::::::::::::::::::::::::Package Benefits ::::::::::::::::::::::::::::::://
      if (PackageTotal > 4) {
        $('.package-swiper-button-next').css("display", "block");
        $('.package-swiper-button-prev').css("display", "block");
        //:::::::::::Swipper Initialize
        myswiper = new Swiper('.s1', {
          slidesPerView: 4,
          simulateTouch: false,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },
        });
        if (PackagePosition > 3) {
          var swipeposition = PackagePosition - 4;
          for (var ii = 0; ii <= swipeposition; ii++) {
            $('.swiper-button-next').click();
          }
        }
      } else {
        //:::::::::::Swipper Initialize
        myswiper = new Swiper('.s1', {
          slidesPerView: 4,
          simulateTouch: false,
        });
        $('.package-swiper-button-next').css("display", "none");
        $('.package-swiper-button-prev').css("display", "none");
      }
      $(".package-swiper-slide").bind("click", function(e) {
        var packageid = $(this).attr("attr-package-id");
        var redirect = $('#' + packageid + 'redirect').attr("rhref");
        redirecturl(packageid, redirect);
      });
      $(".package-swiper-slide").bind("mousemove", function(e) {
        $(".payment-info-box").removeClass("package-selected");
        $(this).addClass("package-selected");
      });
    }
    /*::::::::::::::::::::::::::::::::Dynamic Membership Packages::::::::::::::::::::::::::::::::::::*/
    var redirectcheck = 0;

    function redirecturl(packageid, redirect) {
      if (redirectcheck == 0) {
        var packagetype = package_type_array[packageid];
        var Monthly = MonthlyBasedArray[packagetype];
        _gaq.push(['_trackEvent', PageType, 'LINK', packagetype]);
        ajaxpayment(packagetype, Monthly);
        window.location.href = redirect;
        redirectcheck++;
      }
    }

    function adddcomma(val) {
      while (/(\d+)(\d{3})/.test(val.toString())) {
        val = val.toString().replace(/(\d+)(\d{3})/, '$1' + ',' + '$2');
      }
      return val;
    }

    function ChatWithUS(modelDet = '') {
      console.log('::::::::::::::::::::::ChatWithUS called:::::::::::::::::::::::::::::');
      if (modelDet == 1) {
        ajaxpayment('CHATWITHUS');
      }
      if (scriptloaded == 0) {
        gamoogascriptload();
        setTimeout(function() {
          triggergamooga(1);
          ajaxpayment('Chat of Assistance');
        }, 500);
      } else {
        triggergamooga(1);
        ajaxpayment('Chat of Assistance');
      }
    }
    if (response['GAMOOGA']['DISABLED'] != 1) {
      gamoogascriptload();
    }
    if (response['GAMOOGA']['TIMER'] != '') {
      setTimeout(function() {
        ChatWithUS(); //Live Chat Trigger
      }, response['GAMOOGA']['TIMER']);
    }
  </script>
  <!-- Google Analytics Scripts starts -->
  <script language="javascript">
    var _gaq;
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-BSF6LN3TTX-1']);
    _gaq.push(['_setDomainName', 'MbobileShop.com']);
    _gaq.push(['_trackPageview']);
    (function() {
      var ga = document.createElement('script');
      ga.type = 'text/javascript';
      ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(ga, s);
    })();
  </script>
  <script type="text/javascript">
    var _gaq;
    setTimeout(function() {
      var a = document.createElement("script");
      var b = document.getElementsByTagName("script")[0];
      a.src = document.location.protocol + "//dnn506yrbagrg.cloudfront.net/pages/scripts/0019/1042.js?" + Math.floor(new Date().getTime() / 3600000);
      a.async = true;
      a.type = "text/javascript";
      b.parentNode.insertBefore(a, b)
    }, 1);
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', "UA-BSF6LN3TTX-1"]);
    _gaq.push(['_setDomainName', "MbobileShop.com"]);
    _gaq.push(["_setCustomVar", 1, "User", "M", 2]);
          _gaq.push(["_setCustomVar", 2, "Member", "F", 2]);
              _gaq.push(["_setCustomVar", 3, "Gender", "MF", 2]);
          _gaq.push(['_setAllowLinker', true]);
    _gaq.push(['_trackPageview']);
    (function() {
      var ga = document.createElement('script');
      ga.type = 'text/javascript';
      ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(ga, s);
    })();
    (function(k, e, i, j) {
      k.fn.caret = function(b, l) {
        var a, c, f = this[0],
          d = k.browser.msie;
        if (typeof b === "object" && typeof b.start === "number" && typeof b.end === "number") {
          a = b.start;
          c = b.end
        } else if (typeof b === "number" && typeof l === "number") {
          a = b;
          c = l
        } else if (typeof b === "string")
          if ((a = f.value.indexOf(b)) > -1) c = a + b[e];
          else a = null;
        else if (Object.prototype.toString.call(b) === "[object RegExp]") {
          b = b.exec(f.value);
          if (b != null) {
            a = b.index;
            c = a + b[0][e]
          }
        }
        if (typeof a != "undefined") {
          if (d) {
            d = this[0].createTextRange();
            d.collapse(true);
            d.moveStart("character", a);
            d.moveEnd("character", c - a);
            d.select()
          } else {
            this[0].selectionStart = a;
            this[0].selectionEnd = c
          }
          this[0].focus();
          return this
        } else {
          if (d) {
            c = document.selection;
            if (this[0].tagName.toLowerCase() != "textarea") {
              d = this.val();
              a = c[i]()[j]();
              a.moveEnd("character", d[e]);
              var g = a.text == "" ? d[e] : d.lastIndexOf(a.text);
              a = c[i]()[j]();
              a.moveStart("character", -d[e]);
              var h = a.text[e]
            } else {
              a = c[i]();
              c = a[j]();
              c.moveToElementText(this[0]);
              c.setEndPoint("EndToEnd", a);
              g = c.text[e] - a.text[e];
              h = g + a.text[e]
            }
          } else {
            g = f.selectionStart;
            h = f.selectionEnd
          }
          a = f.value.substring(g, h);
          return {
            start: g,
            end: h,
            text: a,
            replace: function(m) {
              return f.value.substring(0, g) + m + f.value.substring(h, f.value[e])
            }
          }
        }
      }
    })(jQuery, "length", "createRange", "duplicate");
  </script>
  <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-BSF6LN3TTX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
      dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', 'G-BSF6LN3TTX');

    function ga(se, ev, category, gamodule, action, nan) {
      if (se == 'send') {
        gtag('event', category, {
          'event_category': action,
          'event_label': gamodule
        });
      }
    }

    function gaq() {
      this.push = function(ev) {
        if (ev[0] == '_trackEvent') {
          gtag('event', ev[1], {
            'event_category': ev[2],
            'event_label': ev[3]
          });
        }
      }
    }
    var _gaq = new gaq();
  </script>
  <!-- Google Analytics Scripts ends -->
  <!------------------- Gamoooga------------------------------------------->
  <script type="text/javascript">
    $(document).ready(function() {
      var gamogatime1 = response['GAMOOGA']['TIMER'];
      var gamogatime2 = response['GAMOOGA']['TIMERT2'];
      var matriid = "H14550547";
      var startTime = new Date().getTime();
      if (gamogatime2 != 0) {
        setTimeout(gammoga_t2, gamogatime2); //30000 gamoogatime;
        function gammoga_t2(event) {
          var endTime = new Date().getTime();
          var timeSpent = endTime - startTime;
          if (parseInt(timeSpent) >= parseInt(gamogatime2)) {
            $.ajax({
              type: "POST",
              url: "https://mbobileshop.com/payments/gamoogaredis.php",
              dataType: "json",
              data: {
                'timespent': timeSpent,
                'gamogatime1': gamogatime1,
                'gamogatime2': gamogatime2,
                'matriid': matriid,
                'redisset': '1'
              },
              success: function(res) {
                if (res) {
                  console.log(JSON.stringify(res));
                } else {
                  console.log('notredisset');
                }
              }
            });
          }
        }
      }
      setTimeout(gammoga_t1, gamogatime1);

      function gammoga_t1(event) {
        if (gamogatime1 != 0) {
          $.ajax({
            type: "POST",
            url: "https://mbobileshop.com/payments/gamoogaredis.php",
            dataType: "json",
            data: {
              'matriid': matriid,
              'redisset': '0'
            },
            success: function(res) {
              console.log('redis yet to be cleared for t1');
              console.log(res);
              console.log('redis yet to be cleared for t2');
            }
          });
        }
      }
    });
  </script>
  <!------------------- Gamoooga------------------------------------------->
  <script>
    function skipbutton() {
      window.location.href = "";
    }

    function showpayoption() {
      $("#payopshow").hide();
      $(".payopdiv").slideToggle("slow");
    }
    //****************************************ajaxpayment*********************************************************/
    function ajaxpayment(catergory, Monthly = '') {
      var usermatriid = 'H14550547';
      //var fresh = 'fresh';
      var fresh = '';
      var random_val = 0;
      var payorigin = '';
      var nopay = '0';
      var country = '98';
      var productid = ''; /*1,2,3*/
      if (Monthly == 3) productid = 1;
      if (Monthly == 6) productid = 2;
      if (Monthly == 12) productid = 3;
      var logincount = '46';
      var paymentVisitSource = 'MENUSUB';
      var referral = '';
      var offer_details = '';
      var Autorenewalstatus = '0';
      var offerid = '';
      if (offerid == 'undefined' || offerid == '') offerid = 0;
      var parameters = 'catergory=' + catergory + '&type=' + fresh + '&matriid=' + usermatriid + '&country=' + country + '&OptionSelected=' + Monthly + '&payorigin=' + payorigin + '&productid=' + productid + '&NumberOfPayments=' + nopay + '&random_no=' + random_val + "&logincount=" + logincount + "&offerid=" + offerid + "&paymentVisitSource=" + paymentVisitSource + "&referral=" + referral + "&offer_details=" + offer_details;
      $.ajax({
        type: "POST",
        url: "https://mbobileshop.com/payments/paymentfileappend.php?",
        data: parameters,
        success: function(result) {}
      });
    }
    //****************************************ajaxpayment*********************************************************/
    //****************************************eliteinvite*********************************************************/
    function eliteinvite() {
      var ID = 'H14550547';
      var ENCID = 'MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=';
      var TIMECREATED = '1746139838';
      var APPTYPE = '300';
      var ENCMATRIID = 'SDE0NTUwNTQ3';
      var parameters = 'SDBMATRID=' + ID + '&USERTIMEDET=' + TIMECREATED + '&OUTPUTTYPE=2&APPTYPE=' + APPTYPE + '&ID=' + ID + '&ENCMATRIID=' + ENCMATRIID + '&ENCID=' + ENCID + '&Lang=en&PROMOCODE=2';
      $.ajax({
        type: "POST",
        url: "https://api.MbobileShop.com/appdynamicarray/apppromolead.php?",
        data: parameters,
        success: function(result) {
          console.log(result);
          var x = document.getElementById("eliteresponse");
          x.className = "show";
          setTimeout(function() {
            x.className = x.className.replace("show", "");
          }, 2000);
        }
      });
    }
    //****************************************eliteinvite*********************************************************/
  </script>
  <script>
    // Get the modal
    var modal = document.getElementById("myModal");
    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks on the button, open the modal
    btn.onclick = function() {
      modal.style.display = "block";
      document.body.style.overflow = "hidden";
      document.body.style.height = "100%";
    }
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
      document.body.style.height = "auto";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
        document.body.style.height = "auto";
      }
    }
  </script>
  <!-- second one modal start -->
  <script>
    // Get the modal
    var modal = document.getElementById("myModal");
    // Get the button that opens the modal
    var btn1 = document.getElementById("myBtn1");
    console.log("in view");
    // Get the <span> element that closes the modal
    var span1 = document.getElementsByClassName("close")[0];
    // When the user clicks on the button, open the modal
    btn1.onclick = function() {
      modal.style.display = "block";
      document.body.style.overflow = "hidden";
      document.body.style.height = "100%";
    }
    // When the user clicks on <span> (x), close the modal
    span1.onclick = function() {
      modal.style.display = "none";
      document.body.style.overflow = "auto";
      document.body.style.height = "auto";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
        document.body.style.height = "auto";
      }
    }

    function openPrimeBenefitsInfo(id) {
      event.stopPropagation();
      console.log("openPrimeBenefitsInfo==>" + id);
      var elementsUnlimited = document.getElementsByClassName("UNLIMITED_CONTACT_NO_BENEFITS_POPUP" + id);
      for (var i = 0; i < elementsUnlimited.length; i++) {
        elementsUnlimited[i].style.display = "block";
      }
    }

    function closePrimeBenefitsInfo(id) {
      event.stopPropagation();
      console.log("closePrimeBenefitsInfo==>" + id);
      var elementsUnlimited = document.getElementsByClassName("UNLIMITED_CONTACT_NO_BENEFITS_POPUP" + id);
      for (var i = 0; i < elementsUnlimited.length; i++) {
        elementsUnlimited[i].style.display = "none";
      }
    }

    function know_more(pkgId){
      event.stopPropagation(); // Prevents event from bubbling up to parent
      // Get the modal
      var modal = document.getElementById("myModal_tum");
      // Get the <span> element that closes the modal
      var span1 = document.getElementsByClassName("knw_close")[0];

      // When the user clicks on the button, open the modal
      let PackageBenefitHtml = '<a id="' + pkgId + 'redirects" onclick="loading_knwmore(),ajaxpayment(' + pkgId + ',12)" href="https://mbobileshop.com/payments/paymentmode.php?category=' + pkgId + '&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&APPTYPE=300&encip=&PAYMENTOPT=&ip=&Id=SDE0NTUwNTQ3" class="paynow-button knwmore_btn" style="border-radius: 20px !important;padding: 0 0;width: 170px;height: 40px;line-height: 40px;"> Pay Now </a>';

      $("#knw_more_pytm").html(PackageBenefitHtml);

      modal.style.display = "block";
      document.body.style.overflow = "hidden";
      document.body.style.height = "100%";

      // When the user clicks on <span> (x), close the modal
      span1.onclick = function() {
          modal.style.display = "none";
        document.body.style.overflow = "auto";
        document.body.style.height = "auto";
      }

      ajaxpayment(pkgId,12);
    }
    function loading_knwmore(){
      $(".knwmore_btn").html('<img src="https://imgs.MbobileShop.com/bmimgs/mobile-assets/images/bouncing-circles.svg" style="width: 22px;vertical-align: sub;">');
      $(".knwmore_btn").addClass("disabled-link"); // Add CSS class to disable link
    }


    function know_more_smply(pkgId){
      event.stopPropagation(); // Prevents event from bubbling up to parent
      // Get the modal
      var modal = document.getElementById("myModal_smplytum");
      // Get the <span> element that closes the modal
      var span1 = document.getElementsByClassName("smply_knw_close")[0];

      // When the user clicks on the button, open the modal
      let PackageBenefitHtml = '<a onclick="loading_smplyknwmore(),ajaxpayment(' + pkgId + ',12)" href="https://mbobileshop.com/payments/paymentmode.php?category=' + pkgId + '&EncId=MjFiZTk2NWFkNjhhYjE1MGRjMmRjYzk5YmVjNTFiN2IyMGQ1ZTJmM2Q=&Id=SDE0NTUwNTQ3&APPTYPE=300&encip=&PAYMENTOPT=&ip=&Id=SDE0NTUwNTQ3" class="paynow-button smply_knwmore_btn" style="border-radius: 20px !important;padding: 0 0;width: 170px;height: 40px;line-height: 40px;"> Pay Now </a>';

      $("#knw_more_smply_pytm").html(PackageBenefitHtml);

      modal.style.display = "block";
      document.body.style.overflow = "hidden";
      document.body.style.height = "100%";

      // When the user clicks on <span> (x), close the modal
      span1.onclick = function() {
          modal.style.display = "none";
        document.body.style.overflow = "auto";
        document.body.style.height = "auto";
      }

      ajaxpayment(pkgId,12);
    }
    function loading_smplyknwmore(){
      $(".smply_knwmore_btn").html('<img src="https://imgs.MbobileShop.com/bmimgs/mobile-assets/images/bouncing-circles.svg" style="width: 22px;vertical-align: sub;">');
      $(".smply_knwmore_btn").addClass("disabled-link"); // Add CSS class to disable link
    }
  </script>
