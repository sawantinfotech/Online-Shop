<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html lang="en" xmlns="https://www.w3.org/1999/xhtml">
<head>
<title>Mobile Shop - Register or Log In</title>
<meta name="robots" content="noodp">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="keywords" content="Mobile Shop Login, Mobile Shop  Login" />
<meta name="description" content="Register or Log In into MobileShop - The most trusted matrimony site to search lakhs of Mobileshop Brides & Grooms." />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<!--SEO Subdomain URL GET Function -->
<!--SEO Subdomain URL GET Function -->

  <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.mobileshop.com/mobwap/login.php">
  <link rel="canonical" href="https://profile.mobileshop.com/login/login.php">

<script type="text/javascript">var sT=new Date(); var SS=sT.getSeconds();var SST=sT.getTime();</script>
<link rel="shortcut icon" type="image/x-icon" href="https://imgs.mobileshop.com/bmimages/faviconnew.ico" />
<link rel="icon" type="image/ico" href="https://imgs.mobileshop.com/bmimages/faviconnew.ico" />
    <link rel="stylesheet" type="text/css" href="https://imgs.mobileshop.com/bmstyles/mini/commonmini040620190000.css" />

<!--colorbox view enlarge photo css-->
<link rel="stylesheet" href="https://imgs.mobileshop.com/bmstyles/viewenlargephoto.css?random=110420221510">
<!--colorbox view enlarge photo css-->
<link rel="stylesheet" type="text/css" href="https://imgs.mobileshop.com/bmstyles/mini/top-menu-new.css?040620190000" />
<script>
var Jsg_memberid="";
var Jsg_status="";
</script>


<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/jqueryupgrdversion.js?random=110420221510"></script>



<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/colorbox.js?random=110420221510"></script>
<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/mini/jstoragemini1710131511.js"></script>
<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/mini/commonmini28022020183400.js" ></script>	

<!--colorbox view enlarge photo script and css-->
<script src="https://imgs.mobileshop.com/scripts/viewenlargephoto-min.js?random=110420221510"></script>
<script type="text/javascript">
function VwoCookieSet()
{
  var logininfovalue = GetCookie('LOGININFO');
  if(logininfovalue !="" && logininfovalue != null)
  {
      logininfoval = logininfovalue.split("^|");
      return Vwoentrytype  =  logininfoval[7];			
  }
}
var Vwourl = window.location.pathname;
var filenameVwo = Vwourl.substring(Vwourl.lastIndexOf('/')+1);

  var membershiptype= VwoCookieSet();


</script>
<!--colorbox view enlarge photo script and css-->
<script language="javascript">var cmsgreq=0;
var viewfullblockclick="1";</script>

<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/mouseclick-min.js?random=110420221510"></script>

<style>
#menu_block4 .fixed-dropdownbg:after{left: 252px !important;}
</style>

    <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" type="text/css" href="//imgs.mobileshop.com/bmstyles/bootstrap.min.css">
  <!-- Customized CSS -->
  <link rel="stylesheet" type="text/css" href="//imgs.mobileshop.com/bmstyles/seo-style.css">

  <link rel="stylesheet" type="text/css" href="//imgs.mobileshop.com/bmstyles/login-revamp.css?v=30">

  <link rel="stylesheet" type="text/css" href="https://imgs.mobileshop.com/bmstyles/form.css" />
  <style>
  @media only screen and (max-width: 767px) {
    .ftrbtm1 {width: 100%!important;}
  }</style>
    <script>
  $(function(){
  $('#ID,#MIDP,#MID,#otploginID,#forgotpwdid').bind('input', function(){
    $(this).val(function(_, v){
    return v.replace(/\s+/g, '');
    });
  });
  });        

  function chkvalid(){
    var mid = $('#MIDP').val(); 
    if( mid != ''){
      if((validatePhoneNumber(mid) || validateEmail(mid))){            
        if($("#PASSWORD2").val() == ""){
        $("#errorpop").css("display","block");
        $("#errorpop").html("Please enter your Password.");
        if(mobFlagScript == 1){
          $("#PASSWORD2").addClass('err-formfield');
          $("#MIDP").removeClass('err-formfield');
        }
        else{
          $("#PASSWORD2").focus();
        }
        return false;
        } else {
          //Captcha Validation
          captchaTxtDivShown = $("#captchaTxtDiv").css("display");
          //alert(captchaTxtDivShown);
          if (captchaTxtDivShown != "none"){
          if ($("#CAPTCHATEXT").val() == "") {
            $("#errorpop").css("display","block");
            $("#errorpop").html("Please enter text shown in the below image.");
            $("#CAPTCHATEXT").focus();
            return false
            }
          }
        //End Of Captcha Validation
          $("#errorpop").css("display","none");
          $("#loginpopform").submit();
          return true;
        }
      }else if(validateMatriId(mid)){
        if(domainshortnameFlag == 1){
          $("#errorpop").css("display","block");
          $("#errorpop").html(MatriIderr);
          return false
        }else{
          if($("#PASSWORD2").val() == ""){
            $("#errorpop").css("display","block");
            $("#errorpop").html("Please enter your Password.");
              if(mobFlagScript == 1){
                $("#PASSWORD2").addClass('err-formfield');
                $("#MIDP").removeClass('err-formfield');
              }
              else{
                $("#PASSWORD2").focus();
              }
              return false;
          } else {
          //Captcha Validation
          captchaTxtDivShown = $("#captchaTxtDiv").css("display");
          //alert(captchaTxtDivShown);
            if (captchaTxtDivShown != "none"){
            if ($("#CAPTCHATEXT").val() == "") {
              $("#errorpop").css("display","block");
              $("#errorpop").html("Please enter text shown in the below image.");
              $("#CAPTCHATEXT").focus();
              return false
              }
            }
            //End Of Captcha Validation
            $("#errorpop").css("display","none");
            $("#loginpopform").submit();
            return true
            }	
        }
      }
    } 
    else{
      $("#errorpop").css("display","block");
      if(domainshortnameFlag == 1){
        $("#errorpop").css("display","block");
        $("#errorpop").html("Please enter your Mobile Number / Email ID.");
      }else{
        $("#errorpop").css("display","block");
        $("#errorpop").html("Please enter your Mobile Number / Matrimony ID /  Email ID.");
      }
      if(mobFlagScript == 1){
        $("#MIDP").addClass('err-formfield');
      }else{
        $("#MIDP").focus();
      }
      return false;
    }

  }  

  function validatePhoneNumber(mid){
    var mobileregex = /^(\+91-|\+91|0)?\d{7,12}$/;
    return mobileregex.test( mid );
  }   
  function validateEmail(mid) {
    var emailregex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return emailregex.test( mid );
  }  

  function validateMatriId(mid){
    var matriidregex = /^[a-zA-Z][0-9]{5,8}$/;
    return matriidregex.test( mid );
  }   
  </script>
  <div id="result"></div>
<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/mini/jstoragemini1710131511.js"></script>
<script type="text/javascript">
var mail = "";
var loginvalue = jStorage.get("MAILSTAYLOGIN");
var flush = "";
if(flush == 1){
  jStorage.flush();
}
if ((mail == 'Mailer' || mail == 'mailer') && (loginvalue == null || loginvalue =='')) 
{
  $(document).ready(function(){
  $("#result").append("<div style='background:#fffce6;padding:0px 0px;text-align:center;color:#666666;'><form><div align='center' style='padding: 10px;height: 20px;'><div style='width: 100%;'><div class='fleft paddt4' style='width: 50%' align='right'>Your MobileShop profile will be logged in automatically!</div><div class='fleft paddt2 paddl10' align='left'><input checked='checked' id='staylogin' onchange='valueChanged();' type='checkbox'> Keep me logged in (Recommended).</div><div class='fleft paddt2  paddl5' align='left'><a href='javascript:void(0);' id='btnApprovepo' style='cursor:pointer;text-decoration:none;padding:2px 4px;display:none;' onclick='staypopup();' class='txt-hover primaryactbtn-medium clr6 boldtxt'>Submit</a></div><div class='fright' style='padding-top: 3px;' align='right'><a href=''><img src='https://imgs.mobileshop.com/bmimgs/contextual-close-icon.png' height='14'/></a></div><div class='clear'></div></div></div></form></div>");
  });
  jStorage.set('MAILSTAYLOGIN', 1);
}
function valueChanged()
{
    if($('#staylogin').is(":checked"))   
        $("#btnApprovepo").hide();
    else
        $("#btnApprovepo").show();
}
function staypopup(){
  var domain ='mobileshop';
  staylogin_litebox("https://profile."+domain+"matrimony.com/template/staylogin.php");
  $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight").hide();
      $( "#colorbox" ).focus();
  $( "#cboxClose").hide();
    $( "#cboxWrapper" ).focus();
}
function staylogin_litebox(url){
    $.colorbox({open:true, opacity:0.60,open:true,href:url});
} 
</script>

<!-- display instant help script end -->

<!--  -->


<script language="javascript">
  var NODECHAT = "1"; 
</script>
<!-- Ping DOM -->
<!-- Ping DOM -->
<!-- catchpoint - POC -->
<!-- catchpoint - POC -->
</head>

<body onload=document.getElementById('MID').focus() id="close" style="">


<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-WLR9BP2');</script>
<!-- End Google Tag Manager --> 
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WLR9BP2" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
  <div style="display: none;">
    <div id="bmpopbxoverlay"></div>

    <div id="newpopbx" class="bmpopbox relative" style="width: 510px;">

      <div class="paddt10 relative">

        <div style="position:absolute; left:-90px;">
                    <a style="position: absolute; top: 18px; right: 60px;  top: 21px\9; right: 24px\9; display:none" class="closepopup" id="topcloseicon" href="javascript:;" title="Close"><img width="18" height="17" border="0" alt="" src="https://imgs.mobileshop.com/bmimgs/send-mail-pop-close.png"></a>
                    <div id="ResultContainer">



          </div>

        </div>

      </div>

    </div>

  </div>


<center>
<div>



   <div class="container-fluid custom-container xs-none">
  <div class="row">
    <div class="col-lg-12 col-md-12 col-sm-12 col-12">
      <nav class="navbar navbar-expand-lg navbar-light bg-white p-0"">
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="col-lg-11 navbar-nav d-flex align-items-center text-uppercase lato-bold">
          <li class="nav-item">	
          <a class="nav-link" href="https://www.mobileshop.com" ><img src="https://imgs.tamilmatrimony.com/bmimgs/mobileshop-logo.png" title="Mobile Shop" alt="Mobile Shop"></a>
          </li><li class="nav-item ml-3">	  
          <a class="nav-link" href="https://www.mobileshop.com/register/registerform.php?trackid=00510001001&type=internal" target="_blank">Register</a>
          </li><li class="nav-item dropdown mx-3">  
          <a class="nav-link" href="https://profile.mobileshop.com/search/search.php?gaact=SEARCH&gasrc=MENUSUB" target="_blank" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Search
          </a>
          <div class="dropdown-menu cust-dropdown-menu" aria-labelledby="navbarDropdownMenuLink">

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?gaact=reg&gasrc=MENUSUB" target="_blank">Regular search</a>

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?typ=ad&gaact=ad&gasrc=MENUSUB" target="_blank">Advanced search</a>

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?typ=soul&gaact=soul&gasrc=MENUSUB" target="_blank">Soulmate search&trade;</a>

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?typ=key&gaact=key&gasrc=MENUSUB" target="_blank">Keyword Search</a>

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?typ=key&gaact=key&gasrc=MENUSUB" target="_blank">Search by ID</a>

            <a class="dropdown-item" href="https://profile.mobileshop.com/search/search.php?typ=on&gaact=on&gasrc=MENUSUB" target="_blank">Who's Online</a>
          </div>
          </li><li class="nav-item dropdown mx-0 cursor-pointer">    
          <a class="nav-link" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Services
          </a>
          <div class="dropdown-menu cust-dropdown-menu" aria-labelledby="navbarDropdownMenuLink">

            <a class="dropdown-item cursor-pointer" href="https://www.mobileshop.com/assisted/index.php?DomainName=mobileshop&gaact=ASSISTLNK&gasrc=TOPNAV" target="_blank">Assisted Services</a>

            <a class="dropdown-item" href="https://www.mobileshop.com/matrimony-outlets.php" target="_blank">140+ Matrimony Branches</a>

            <a class="dropdown-item" href="https://www.weddingbazaar.com/" target="_blank">Wedding Bazaar</a>

            <a class="dropdown-item" href="https://www.mandap.com/" target="_blank">Mandap</a>

            <a class="dropdown-item" href="https://www.happymarriages.com?gaact=happymar&gasrc=MENUSUB" target="_blank">Happy Marriages</a>
          </div>
          </li><li class="nav-item ml-3"> 
          <a class="nav-link" href="https://www.mobileshop.com/payments/paymentoptions.php?hpupglink&gaact=PAY&gasrc=MENUSUB">Upgrade</a>
          </li>
        </ul><div class="dropdown mt-3 pt-2"><img src="//imgs.mobileshop.com/bmimgs/hp-helpicn.png" width="23" height="23" class="cursor-pointer" data-toggle="dropdown">

            <div class="dropdown-menu dropdown-content-quest dropdown-content-quest1" style="left: -197px;top: 30px;padding-bottom: 20px !important;">
            <div id="hp-help-div" class="hp-help-ttip" style="width:310px">
                  <div class="hp-help-ttip-arw">
                    <div class="hp-help-arw"></div>
                  </div>
                  <div class="hp-help-ttipbg">
                    <div style="width:;letter-spacing:0.4px;">
                      <div id="div_help" class="fleft mediumtxt" style="width:; color:#777;">
                        <div class="paddt5 paddl10">
                          <div class="helpline-icon">
                            <div class="fixed-helpline-icon">
                              <div class="hdtxt1" style="font-family:Lato;font-weight: 700;">24x7 HELP : </div>
                              <div class="paddt5 hdtxt" id="cntryphno" style="font-family:Lato;font-weight: 700;"><span class="mediumtxt">INDIA : +91 7538896555</span></div>
                            </div>
                          </div>
                          <div class="hdot paddt20" id="marginhdot" style="width: 250px; margin: 0px;"><!--  --></div>
                          <div>
                            <div class="fleft paddt5 paddl10" style="width:;">
                              <!--<div id="displayIN" style="display: block;"><div class="fleft paddt5" style="width:85px;"><b>INDIA</b></div><div class="fleft paddt5"> : 7538896555</div></div>
                              <div class="clear"></div>-->
                              <div id="displayUAE" style="display: block;"><div class="fleft paddt5" style="width:85px;"><b>UAE</b></div><div class="fleft paddt5"> : +971 525060879</div></div>
                              <div class="clear"><!-- --></div>
                            </div>
                          </div>
                                                    <div class="hdot" id="marginhdot" style="width: 250px;position: absolute;padding-top: 28px;"><!--  --></div>
                                                    <div id="div_help" class="fleft" style="padding-top:30px;">
                                                            <a href="/contact-us.php?viewtab=livehelp&amp;gaact=HP&amp;gasrc=HELPLHTAMIL" class="menunrml clr7 arrow">Live Help</a>
                                                            <a href="/contact-us.php?gaact=HP&amp;gasrc=HELPCONTAMIL" class="menunrml clr7 arrow">Contact Us</a>

                                                            <a href="/contact-us.php?viewtab=feedback&amp;gaact=HP&amp;gasrc=HELPFEEDBACKTAMIL" class="menunrml clr7 arrow">Feedback</a>
                                                            <a href="/contact-us.php?viewtab=businessqueries&amp;gaact=HP&amp;gasrc=HELPBQTAMIL" class="menunrml clr7 arrow">Business Queries</a>
                                                    </div>
                                                    <div class="clear"><!--  --></div>
                        </div>
                      </div>

                    </div>
                  </div>
                </div>
            </div>
          </div> 



        </div>
      </nav>
    </div>
  </div>
   </div>
<style type="text/css">
  .errorbg{border:1px solid #CE3737; padding:3px;}
  #topnavlog{height:auto !important; margin-bottom:0px !important;}
  .topnavlog{padding:8px 0px 8px 0px !important;}
    #topnavlog ul li.icon{padding:3px 5px 1px 7px !important;}
  #web-notify-icon-placeholder span{margin-left:5px !important}
  #menu1 #fixed-div_help a.arrow{background-position:0 -506px}
  .scrolluppos-open1{top:26px !important; left:-42px !important; margin-left:0px !important; z-index:100000 !important; position:absolute !important;}
  .cometchat_traycontent,.cometchat_traycontent span,.cometchat_traycontent span:hover {text-shadow: none;  text-shadow: none !important;}
  .cometchat_traycontent span,#cometchat_trayicon_webnotify_popup_content1 a{color:#0274CB !important;}
  .cometchat_traycontent span:hover{color:#0274CB !important;} .wnote{width:250px}
  .cometchat_dashboardcount a:hover{text-shadow: none;text-shadow: none;}
  dd a:hover{text-shadow: none !important;} 
  .cometchat_dashboardcount:hover{text-shadow: none;	text-shadow: none !important;}
  .cometchat_dashboardlist a:hover{text-shadow: none;	text-shadow: none !important;}
  #cometchat_trayicon_webnotify_popup_content2{padding:0px 8px 5px 0px !important;}
  #cometchat_trayicon_webnotify_popup_content1{padding:0px 8px 5px 0px !important;}
  .top_notifycount_pos{top:0px !important; margin-left:-10px !important; float:left;}
  .scroll_notifycount_pos{top:-9px !important; margin-left:-10px  !important; float:left;}
  #topnavlog ul li span.fixed-webnotify-icon-off{padding-right:0px;}
  #topnavlog ul li span.fixed-webnotify-icon-on{padding-right:0px;}
  .login-pop-div{right: -2px; top: -32px;}

</style><style>
.blink_me { -webkit-animation-name: blinker; -webkit-animation-duration: 2s; -webkit-animation-timing-function: linear; -webkit-animation-iteration-count: infinite; -moz-animation-name: blinker; -moz-animation-duration: 1s; -moz-animation-timing-function: linear; -moz-animation-iteration-count: infinite; animation-name: blinker; animation-duration: 1s; animation-timing-function: linear;  animation-iteration-count: infinite; }
@-moz-keyframes blinker {  0% { opacity: 1.0; }50% { opacity: 0.0; }100% { opacity: 1.0; }}
@-webkit-keyframes blinker {  0% { opacity: 1.0; }50% { opacity: 0.0; }100% { opacity: 1.0; }}
@keyframes blinker {  0% { opacity: 1.0; }50% { opacity: 0.0; }100% { opacity: 1.0; }}
</style>
<script type="text/javascript" src="https://imgs.mobileshop.com/scripts/topnav1024.js?dt=28042015"></script>
 <!-- Browser profile by Start-->
 <!-- Browser profile by End-->
<style>
    .errorbg{
            border: 1px solid #ce3737!important;
    }

  .loginoverlay {position: fixed;top: 0;bottom: 0;left: 0;right: 0;background: rgba(0, 0, 0, 0.7);transition: opacity 500ms;
visibility: hidden;opacity: 0;z-index:99;}
.loginoverlay:target {visibility: visible !important;opacity: 1;}
.loginpopup {padding: 29px;background: #f1f1f1;border-radius: 10px;width: 342px;position: relative;transition: all 5s ease-in-out;position: absolute;top: 20%;left: 36%;}
.hp-button {width: 63px;-webkit-border-radius: 2px;-moz-border-radius: 2px;border-radius: 2px;background: #ff7c0b;color: #fff;cursor: pointer;height: 30px;border: none!important;display: inline-block;font-family: arial;margin: 0;outline: medium none;text-decoration: none;}
.hp-txtBox {border: 1px solid #e0e0e0;background-color: #fff;color: #777;padding: 7px;font: bold 11px arial;}


.dropdown-menu.dropdown-content-quest:before {content: "";position: absolute;right: 92px;top: -10px;width: 0;height: 0;border-style: solid;border-width: 0 10px 10px 10px;border-color: transparent transparent #f0f0f0 transparent;}
.dropdown:hover .dropdown-content-quest {background-color: #f0f0f0;margin-top: 12px;border-radius: 20px;border: 0;}
.dropdown:hover .dropdown-content-quest, .dropdown:hover .cust-dropdown-menu {display: block;}
.browse-by-section {float: left;width: 86%;margin-top: 18px;position: absolute;top: 19px;}
.browse-login {float: left;border: 1px solid #ff9902;padding: 5px 30px;font-size: 12px;font-family: 'Lato';border-radius: 10px;color: #ff9902;font-weight: bold;text-transform: uppercase;margin-top: 5px;cursor: pointer;margin-left: 16px;margin-right: 16px;}
.browse-login a {color: #ff9902;text-decoration: none;}
.browse-login a:hover {color: #ff9902;text-decoration: none;}
.browse-bar {float: left;margin-top: 7px;}

.paddr5 {padding-right: 5px;}
.dropdown-content {padding: 10px 0 15px 0;display: none;position: absolute;background-color: #fff;width: auto;overflow: auto;z-index: 1;top: 43px;right: 165px;border-radius: 12px;box-shadow: 0 2px 13px 0 rgb(0 0 0 / 16%);}
.dropbtn1:after {content: '';background: url(//imgs.mobileshop.com/bmimgs/bmhp-selectarw.png) no-repeat!important;width: 12px!important;height: 7px!important;background-position: 0px 0px!important;display: inline-block!important;top: 0px!important;left: 0px!important;position: relative!important;}
.hp-tab-hd {float: left;width: 140px;}
.chiptablink, .desp-drpdwn, .ftr-acc-bdr, .pointer, .slidernext, .sliderprev, .swiper-slide, .tablink, a, button, select {outline: 0;-webkit-tap-highlight-color: transparent;}
.tablink {font-size: 16px;font-weight: 700;color: #000;font-family: Lato;padding: 15px 26px;text-align: left;cursor: pointer;letter-spacing: .6px;}
.hptab-cnt {float: left;width: auto;}
.bm-animate-fading {animation-name: fadeInOpacity;animation-iteration-count: 1;animation-timing-function: ease-in;animation-duration: .4s;}
.tabfleft {float: left;}
.browselink ul li {list-style: none;text-align: left;padding: 15px 25px;font-size: 14px;font-weight: 700;font-family: Lato;letter-spacing: .5px;}
.browselink ul li a {text-decoration: none;cursor: pointer;color: #000;font-weight: 400;letter-spacing: .6px;font-size: 14px;}
.dropdown-content a {display: block;}
.bm-green {color: #00a03a;background: #f1f1f1;}

@media only screen and (max-width: 767px) {
.dropbtn1:after {background: 0 0!important;width: 23px;height: 20px;position: absolute;top: 5px;left: 4px;}
.desk-none {display: block!important;}
.mob-none {display: none!important;}
.fright {float: right;}
.dropdown-content {width: 330px!important;top: 64px!important;left: 15px!important;padding-bottom: 5px;padding-left: 15px;padding-top: 15px;position: fixed!important;}
.show {z-index: 99999999!important;}
.show {display: block;opacity: 1;animation-name: fadeInOpacity;animation-iteration-count: 1;animation-timing-function: ease-in;animation-duration: .4s;}
.dropdown-content {padding: 10px 0 15px 0;display: none;position: absolute;background-color: #fff;width: auto;overflow: auto;z-index: 1;top: 48px;left: 0;border-radius: 12px;box-shadow: 0 2px 13px 0 rgb(0 0 0 / 16%);}
.hp-tab-hd {float: none;width: 100%;overflow-x: auto;white-space: nowrap;scrollbar-color: #fff #fff;height: 55px!important;}
.bm-green {color: #fff;background: #00a03a;}
.tablink {font-size: 12px;padding: 7px 15px;letter-spacing: .4px;display: inline-block;border: 1px solid #e1e1e1;border-radius: 17px;margin-right: 6px;border-radius: 20px;}
.hptab-cnt {float: none;width: 100%;display: inline-block;}
.tabfleft {display: inline-block;width: 33%;}
.tabfleft {float: left;}
.browselink ul li {list-style: none;text-align: left;padding: 0 0px 17px 5px!important;font-size: 11px;font-weight: 700;font-family: Lato;letter-spacing: .5px;float: left;}
.browselink ul li a {font-size: 12px;text-overflow: ellipsis;overflow: hidden;width: 90px;white-space: nowrap;}
.dropdown-content.ppshw.desk-none {display: none!important;}
}

.fixed-login-popup-new-1024, .fixed-login-popup-new-800 {
  background-color: #fff;
}
.already-text {
  font-size: 16px;
    font-family: 'Lato';
    font-weight: 500;
    letter-spacing: 0.42px;
    text-shadow: 0px 0px;
    margin-right: 10px;
}
.login-button-cta {
  font-family: 'Lato';
    color: #E06506 !important;
    background: #fff;
    border: 1px solid #E06506;
    padding: 7px 29px;
    font-size: 14px;
    border-radius: 10px;
}

.login-already-section {
  position: absolute;
  margin-top: 6px;
  margin-right: -48px;
  right: 269px;
  display1: none;
  z-index: 99999;
}
.ss-header-top {
  margin-top: -7px;
    margin-right: -40px;
}
body .ss-header-top {
    font-size: 12px;
  line-height: normal;
}
body .ss-header-top .small {
    font-size: 13px;
    font-weight: 700;
}

@media only screen and (min-width: 768px) and (max-width: 1281px) { 
  .login-already-section {
    margin-right: -80px;
  }
}
@media only screen and (min-width: 1400px) and (max-width: 1450px) { 
  .login-already-section {
    margin-right: -10px;
  }
}
@media only screen and (min-width: 1450px) and (max-width: 1500px) { 
  .login-already-section {
    margin-right: 20px;
  }
}
@media only screen and (min-width: 1501px) and (max-width: 1610px) { 
  .login-already-section {
    margin-right: 75px;
  }
}
@media only screen and (min-width: 1611px) and (max-width: 1710px) { 
  .login-already-section {
    margin-right: 127px;
  }
}
@media only screen and (min-width: 1710px) and (max-width: 1930px) { 
  .login-already-section {
    margin-right: 233px;
  }
}
@media only screen and (min-width: 1931px) and (max-width: 2561px) { 
  .login-already-section {
    margin-right: 552px;
  }
}

</style>
<script>
   function topnavlogincheck(){
     var mid = $('#ID').val(); 
       if((validatePhoneNumber(mid) || validateEmail(mid) || validateMatriId(mid)) && mid != '' && mid != 'ID / E-mail / Mobile Number'){
            if($(".PASSWORD2").val() == "" || $(".PASSWORD2").val() == "password")
      {
                $(".PASSWORD2").addClass('errorbg').focus();

        return false;
      }
        return true
           }
    else{
        $("#ID").addClass('errorbg').focus();
        return false;
    }
  }  

     function validatePhoneNumber(mid){
          var mobileregex = /^(\+91-|\+91|0)?\d{7,12}$/;
  return mobileregex.test( mid );
}   
     function validateEmail(mid) {
           var emailregex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailregex.test( mid );
}  

     function validateMatriId(mid){
          var matriidregex = /^[a-zA-Z][0-9]{5,8}$/;
  return matriidregex.test( mid );
} 
</script>
<script type="text/javascript">

  function otplogin(e) {
  var domain = "imgs.mobileshop.com"; 
  var secureurl = "https://";
    url = secureurl + curDomain + "/login/loginviaotp.php";

    $.colorbox({
        href: url, 
        onLoad: function() {
            $("iframe").css("visibility", "hidden");
      $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight").hide();
      $("#cboxClose").css({
        "background":"url("+secureurl+domain+"/bmimgs/forgot-password-close.gif)",
        "background-repeat":"no-repeat",
        "right":"10px",
        "top":"10px"
      });
      $("#otpform").hide();
      $("#cboxOverlay").css({
        "background-color":"black",
        "background-repeat":"no-repeat",
        "opacity":"0.60 "});			
        },
        onClosed: function() {
            $("iframe").css("visibility", "visible");
            $("#" + e).attr("href", "javascript:void(0);");
            $("#" + e).attr("class", "");
      $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight").show();
      $("#cboxClose").css({
        "background":"url("+secureurl+domain+"/bmimgs/litebox/controls.png)",
        "background-repeat":"-25px 0",
        "background-position":"-25px 0"

      });
      $("#cboxOverlay").css({
        "background-color":"rgba(0, 0, 0, 0)",
        "background-image":"url("+secureurl+domain+"/bmimgs/litebox/overlay.png')",
        "opacity":"0.9"});
        },
        onComplete: function() {
            $("#otplogin").focus()
        }
    })
}

  function forgotpasswd(e) {
  var domain = "imgs.mobileshop.com"; 
  var secureurl = "https://";
    url = secureurl + curDomain + "/login/forgotpassword.php";
    $.colorbox({
        href: url, 
        onLoad: function() {
            $("iframe").css("visibility", "hidden");
      $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight").hide();
      $("#cboxClose").css({
        "background":"url("+secureurl+domain+"/bmimgs/forgot-password-close.gif)",
        "background-repeat":"no-repeat",
        "right":"10px",
        "top":"10px"
      });
      $("#otpform").hide();
      $("#cboxOverlay").css({
        "background-color":"black",
        "background-repeat":"no-repeat",
        "opacity":"0.60 "});			
        },
        onClosed: function() {
            $("iframe").css("visibility", "visible");
            $("#" + e).attr("href", "javascript:void(0);");
            $("#" + e).attr("class", "");
      $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight").show();
      $("#cboxClose").css({
        "background":"url("+secureurl+domain+"/bmimgs/litebox/controls.png)",
        "background-repeat":"-25px 0",
        "background-position":"-25px 0"

      });
      $("#cboxOverlay").css({
        "background-color":"rgba(0, 0, 0, 0)",
        "background-image":"url("+secureurl+domain+"/bmimgs/litebox/overlay.png)",
        "opacity":"0.9"});
        },
        onComplete: function() {
            $("#forgotpwd").focus()
        }
    })
}

</script>

<script>
function browseFunction() {document.getElementById("myDropdown").classList.toggle("show");$("#togpopshow").addClass("togpop");$("body").addClass("overflw");}
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');$("#togpopshow").removeClass("togpop");$("body").removeClass("overflw");
      }
    }
  }
}
// Hide Accordion body on click outside
$('.dropdown-content').on('click', function(e) {e.stopPropagation();});

function openLink(evt, animName) {
  var i, x, tablinks;x = document.getElementsByClassName("browsetab");for (i = 0; i < x.length; i++) {x[i].style.display = "none";}
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {tablinks[i].className = tablinks[i].className.replace("bm-green", "");}
  document.getElementById(animName).style.display = "block";evt.currentTarget.className += " bm-green";
}
</script>	<div><div class='fleft' id='lp-container' style='width:100%;margin:0px auto;'><div class='login-bg-mobile-mobileshop'><div class='wrapper-max'><div style="z-index: 1005; margin-left: 714px; margin-top: 0px; position: absolute;display:none; cursor: default;" class="width225" id="showcountrie">
      <div style="position:absolute; z-index:100001;" class="width225">
        <div  class="fright" style="background:#fff; border-width: 1px 1px 0px; border-style: solid solid none; border-color: #00A651;"><div style="text-align:center; padding: 5px 6px;"><span class="morearrow link mediumtxt">All Countries</span></div></div><div style="clear:both;"><!--  --></div>
        <div style="background:#fff; border-right: 1px solid #00A651; border-width: 0px 1px 1px; border-style: none solid solid; border-color:#00A651">
          <div style="border-top: 1px solid #00A651; height: 1px;margin-right: 94px;"><!--  --></div>
          <div class="padd10">
            <div class="smalltxt">
              <div class="boldtxt">INDIA</div>
              <div class="paddt2">
              <span id="phind"><!--  --></span>
              </div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">USA</div>
              <div class="paddt2"><span id="phusa"><!--  --></span></div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">UK</div>
              <div class="paddt2"><span id="phuk"><!--  --></span></div>
            </div>											
            <div class="smalltxt paddt4">
              <div class="boldtxt">SINGAPORE</div>
              <div class="paddt4"><span id="phsing"><!--  --></span></div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">UAE</div>
              <div class="paddt2"><span id="phuae"><!--  --></span></div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">CANADA</div>
              <div class="paddt2"><span id="phcan"><!--  --></span></div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">MALAYSIA</div>
              <div class="paddt2"><span id="phmal"><!--  --></span></div>
            </div>
            <div class="smalltxt paddt4">
              <div class="boldtxt">AUSTRALIA</div>
              <div class="paddt2"><span id="phaus"><!--  --></span></div>
            </div>
          </div>
        </div>
      </div>
    </div></div><!-- <script type="text/javascript"> hp_phone(); loadphone(); </script> -->
<script type="text/javascript">
    var secureurlVar  = "https://";
  </script>




<script language="javascript">
      function popup_litebox11(url){
      var urlrep = url.replace("https://profile."+DOMAINARRAY['domainnameshort']+"matrimony.com","");
      if(url.indexOf("privformmyhome.php") > -1){
      $("#newpopbx").newcolorbox(urlrep);
      return false;
      } 
      //$.colorbox({open:true, opacity:0.60,open:true,href:url});
      } 
</script>

    <div class="fixed-topnavbg fleft " id="fixed-topnavbg" style="width: 100%;background: #fff;" onclick="regPDLogTrackAjax('header-part')"><div class="wrapper-max">
      <div class="fleft fixed-newmenu-1024 menu-width" id="menu1" style="">

        <div class="middle" style="width:1088px !important; height:45px;padding-top: 8px;">
            <div class="pipe fixed-nav-sep paddt5 paddr20" style="display:block ; background:none !important;margin-right: 95px;" id="logo_outer"><span class="matrimony-tag-text">From Matrimony.com Group</span><a href="https://www.mobileshop.com"><img height="48" width="150" border="0" title="Mobile Shops" alt="Mobile Shops" src="https://imgs.mobileshop.com/bmimgs/mailers/mailerlogo/new/mobileshop-matrimony-logo.png" /></a></div>
            <div class="pipe fixed-nav-sep" style="background:none !important">
            <div id="tab0" class="navbg">
              <span id="overbg1" class="midalog" style="padding-left1:0px !important; padding-right1:30px !important;"><a href="https://www.mobileshop.com/register/registerform.php?trackid=00510001001&type=internal" title="Register Free" alt="Register Free">Register</a><img src="https://imgs.mobileshop.com/bmimgs/trans.gif" width="8" height="7" border="0" align="absmiddle" style="display:none;" name="arrow_profile" id="arr1" class="menu-arrow" /></span>
            </div>
            <div style="color:#000; display:none; z-index:10001;" onmouseout="subTabTimeout('menu_block1','tab0','1');" onmouseover="mcancelclosetime();" id="menu_block1"></div>
          </div>

          <div class="pipe fixed-nav-sep">
            <div id="tab1" class="navbg ">
              <a title="Search" alt="Search" class="fleft midalog"  onmouseover="showmenubar('menu_block2')"  onmouseout="hidemenubar('menu_block2')" href="https://profile.mobileshop.com/search/search.php?gaact=SEARCH&gasrc=MENUSUB">Search</a>
              <div style="position:absolute;margin-left:-1px; margin-top:47px!important; *margin-left:-91px;  display:none;z-index:10001;" onmouseover="showmenubar('menu_block2')" onmouseout="hidemenubar('menu_block2')" id="menu_block2" class="menublock">
                <div style="position:absolute;margin-left:1px!important; margin-top:10px !important;z-index:10001; display:inline;width:260px;" class="fixed-drpdwnmenu fixed-drop-shadow fixed-dropdownbg">
                  <div id="fixed-div_search" class="fixed-div_search">
                    <a style="display:inline;margin-top:10px;" href="https://profile.mobileshop.com/search/search.php?gaact=reg&gasrc=MENUSUB" class="menunrml arrow">Regular search</a>
                    <a href="https://profile.mobileshop.com/search/search.php?typ=ad&gaact=ad&gasrc=MENUSUB" class="menunrml arrow" style="display:inline;">Advanced search with subcaste & gothra</a>
                    <a href="https://profile.mobileshop.com/search/search.php?typ=soul&gaact=soul&gasrc=MENUSUB" class="menunrml arrow" style="display:inline;">Soulmate search&trade;</a>
                      <a href="https://profile.mobileshop.com/search/search.php?typ=key&gaact=key&gasrc=MENUSUB" class="menunrml arrow" style="display:inline;">Keyword search</a>
                      <a href="javascript:void(0);" onclick="show_hide_sbid('show');" id="msbid" class="menunrml arrow" style="display:inline">Search by ID</a><div class="clear"><!--  --></div>
                      <div id="sbid" style="display:none;" class="paddl15 paddb10">
                        <div class="paddb2 smalltxt" id="matri-text">Enter the Matrimony ID of the member</div>
                        <form onsubmit="return frmvalidbyid();" method="post" name="MatriFormSBID"><input type="text" tabindex="1" class="inputtext" style="width:75px; padding:3px;" id="SSID" name="BMID">&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" class="button vsmall" value="View Profile"></form>
                       </div>
                      <a href="https://profile.mobileshop.com/search/search.php?typ=on&gaact=on&gasrc=MENUSUB" class="menunrml arrow" style="display:inline;margin-bottom:5px;">Who's Online</a><div class="clear"><!--  --></div>
                  </div>
                </div>
              </div>
            </div>


          </div>

          <div class="pipe fixed-nav-sep">
            <div id="tab5" class="navbg">
              <a class="fleft midalog" onmouseover="showmenubar('menu_block8')" onmouseout="hidemenubar('menu_block8')"   title="Services" alt="Services">Services</a>
                <div style="position:absolute;margin-left:-1px; margin-top:47px!important; *margin-left:-104px;  display:none;z-index:10001;" onmouseover="showmenubar('menu_block8')" onmouseout="hidemenubar('menu_block8')"  id="menu_block8" class="menublock">
                <div style="position:absolute;margin-left:1px!important; margin-top:10px !important;z-index:10001;" class="fixed-drpdwnmenu fixed-drop-shadow fixed-dropdownbg">
                  <div id="fixed-div_search" class="fixed-div_search" style="width:182px;"><a href="https://www.mobileshop.com/assisted/index.php?DomainName=mobileshop&gaact=ASSISTLNK&gasrc=TOPNAV" class="menunrml arrow" id="ampftg" target="_blank" style="display:inline;margin-top:10px;width:89% !important;">Assisted Service</a>
                    <a href="https://www.mobileshop.com/matrimony-outlets.php" target="_blank" class="menunrml arrow" style="display:inline;width:89% !important;"><span id="outletcountval"><!--  --></span>+ Matrimony Branches</a>
                    <a href="https://www.weddingbazaar.com/" target="_blank" class="menunrml arrow" style="display:inline;width:89% !important;">Wedding Bazaar</a><a href="https://www.happymarriages.com?gaact=happymar&gasrc=MENUSUB" target="_blank" class="menunrml arrow" style="display:inline;margin-bottom:5px;width:89% !important;">Happy Marriages</a>

                    <div class="clear"><!--  --></div>

                  </div>
              </div>
            </div>
            </div>
          </div>

          <div class="pipe fixed-nav-sep" id="mobi-apps-tab2">
            <div id="tab5" class="navbg ">
              <a class="fleft midalog" onmouseover="showmenubar('menu_block9')" onmouseout="hidemenubar('menu_block9')" href="https://www.mobileshop.com/matrimony-mobile-apps?gaact=MOBILETXTLINK&gasrc=MENUSUB" title="Mobile" alt="Mobile">Mobile</a>
                <div style="position:absolute;margin-left:-1px; margin-top:47px!important; *margin-left:-104px;  display:none;z-index:10001;" onmouseover="showmenubar('menu_block9')" onmouseout="hidemenubar('menu_block9')"  id="menu_block9" class="menublock">
                <div style="position:absolute;margin-left:1px!important; margin-top:10px !important;z-index:10001;padding-bottom:10px;" class="fixed-drpdwnmenu fixed-drop-shadow fixed-dropdownbg">
                  <div id="fixed-div_search" class="fixed-div_search" style="width:155px;"><a href="https://play.google.com/store/apps/details?id=com.mobileshop" target="_blank" class="menunrml arrow" style="display:inline;margin-top:10px;width:87% !important;">Android</a>									<a href="https://itunes.apple.com/us/app/mobileshop-matrimonial/id465923141?mt=8" target="_blank" class="menunrml arrow" style="display:inline;width:87% !important;">iPhone</a>										<a href="https://itunes.apple.com/us/app/mobileshop-matrimonial/id465923141?mt=8" target="_blank" class="menunrml arrow" style="display:inline;width:87% !important;">iPad</a>
                    <a href="https://www.windowsphone.com/en-US/apps/6b27f240-e608-435f-9e00-5ab66e08bd78" target="_blank" class="menunrml arrow" style="display:inline;width:87% !important;">Windows 8</a>
                    <a href="https://appworld.blackberry.com/webstore/content/57621?lang=en" target="_blank" class="menunrml arrow" style="display:inline;width:87% !important;">BlackBerry</a>
                    </div>
                </div>
              </div>
            </div>
          </div>

          <div class="pipe fixed-nav-sep">
            <div id="tab2" class="navbg ">
              <span id="overbg3" class="midalog" style="padding-left1:20px !important;"><a style="float:left;" class="" href="https://www.mobileshop.com/payments/paymentoptions.php?hpupglink&gaact=PAY&gasrc=MENUSUB" title="Become a paid member" alt="Become a paid member">Upgrade</a><img src="https://imgs.mobileshop.com/bmimgs/trans.gif" width="8" height="7" border="0" align="absmiddle" style="display:none;" name="arrow_profile" id="arr3" class="menu-arrow" /></span>
            </div>

            <div style="position:absolute; margin-left:-1px!important; margin-top:49px!important; display:none;z-index:10001;" onmouseout="subTabTimeout('menu_block3','tab2','3');" onmouseover="mcancelclosetime();" id="menu_block3" class="menublock"></div>
          </div><div class="pipe fixed-nav-sep" style="background:none;float:right;margin-right: -25px;margin-top: -11px;">
            <div id="tab3" class="navbg ">
              <a title="Help" alt="Help" class="fleft midalog" href="https://www.mobileshop.com/contact-us.php?gaact=HELPMAINLINK&gasrc=TOPNAV" onmouseover="showmenubar('menu_block4')" onmouseout="hidemenubar('menu_block4')"><img src="//imgs.mobileshop.com/bmimgs/desktop-images/prelogin-revamp-images/hp-helpicon.svg" style="margin-right: 7px;"> Help <img src="//imgs.mobileshop.com/bmimgs/homepage-revamp-images/hp-helpicn-dropdown.svg" style="margin-left: 4px;margin-top: 4px;"></a>
                <div style="position:absolute;margin-left:-431px; margin-top:47px!important; *margin-left:-504px;  display:none;z-index:10001;" onmouseover="showmenubar('menu_block4')" onmouseout="hidemenubar('menu_block4')" id="menu_block4" class="menublock">

                <div style="position:absolute;margin-left: 207px!important;margin-top:10px !important;z-index:10001;" class="drpdwnmenu fixed-drop-shadow fixed-dropdownbg">
                  <div style="width:280px;">
                    <div id="fixed-div_help" class="fleft smalltxt" style="width:257px; color:#777;margin-bottom: 12px;">
                      <div class="paddt10 paddl10">
                        <div class="fixed-helpline-icon">
                          <div class="boldtxt">24x7 HELP : </div>
                          <div class="boldtxt hdtxt">INDIA : 0-8144-99-88-77</div>
                        </div>

                        <div class="hdot paddt5" style="margin:0px 0px 0px 0px"></div>
                        <div class="fleft">
                        <div style="display:none"><div class="fleft paddt5 paddl10" style="width:80px;"><b>INDIA</b></div><div class="fleft paddt5"> : 0-8144-99-88-77</div></div><div class="clear"><!-- --></div>
                                                <div style="display:block"><div class="fleft paddt5 paddl10" style="width:80px;"><b>UAE</b></div><div class="fleft paddt5"> : +971 525060879</div></div><div class="clear"><!-- --></div>
                        </div>
                        <div class="clear"><!--  --></div>
                                                <div class="hdot paddt5" style="margin:0px 0px 0px 0px"></div>
                                                <div id="fixed-div_help"  class="fleft paddt15" style="width:184px;"><div class=""><a href="https://www.mobileshop.com/contact-us.php?viewtab=livehelp&gaact=CUSTOMERCHAT&gasrc=TOPNAV" class="menunrml arrow" style="display:block;width:99% !important;">Chat with Customer Care</a></div><div class=""><a href="https://www.mobileshop.com/faq.php?gaact=FAQ&gasrc=TOPNAV" class="menunrml arrow" style="display:block;width:99% !important;">FAQ</a></div>
                                                    <div class=""><a href="https://www.mobileshop.com/contact-us.php?gaact=CONTACTUS&gasrc=TOPNAV" class="menunrml arrow" style="display:block;width:99% !important;">Contact Us</a></div>

                                                    <div class=""><a href="https://www.mobileshop.com/contact-us.php?viewtab=feedback&gaact=FEEDBACK&gasrc=TOPNAV" class="menunrml arrow" style="display:block;width:99% !important;">Feedback</a></div>
                                                    <div class=""><a href="https://www.mobileshop.com/contact-us.php?viewtab=businessqueries&gaact=BQUERIES&gasrc=TOPNAV" class="menunrml arrow" style="display:block;width:99% !important;">Business Queries</a></div>
                                                </div>
                                                <div class="clear"><!--  --></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>


          </div></div>

    </div><div class="clear"><!--  --></div>

  </div></div><br clear="all"><div class="sites-margin"></div><!--{ Dont delect this -->

<br clear="all">

<div id="phnodiv" style="display:none;"></div>

<script type="text/javascript" language="javascript"> loadoutlet("outletcountval"); </script>

<link rel="stylesheet" href="https://imgs.mobileshop.com/bmstyles/prelogin-revamp/prelogin-style.css">

<style>
@font-face {
  font-family: 'Lato';font-style: normal;font-weight: 400;font-display: swap;
  src: local('Lato'), local('Lato-Regular'), url(https://imgs.bengalimatrimony.com/bmstyles/font/lato-regularnew.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
@font-face {
  font-family: 'Lato';font-style: normal;font-weight: 700;font-display: swap;
  src: local('Lato Bold'), local('Lato-Bold'), url(https://imgs.bengalimatrimony.com/bmstyles/font/lato-bold-ui.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
    font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
    src: url('https://imgs.bengalimatrimony.com/bmstyles/font/roboto-regular.woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
.wrapper-max {
  width: 1088px;
}
.wrapper-max #menu1 .midalog, #menu1 .midalog a, .wrapper-max .midalog-active {
    color: #000000 !important;
  padding-left: 5px !important;
  display: flex;
    align-items: center;
  font-size: 16px;
    font-weight: lighter;
    font-family: 'Roboto';
}
#menu1 .midalog a:hover {
  color: #000000 !important;
}
#menu1 .pipe {
  display: block !important;
  margin-top: -8px;
}
.fixed-top_header_fixed {
  padding-top: 11px;
}
.fixed-nav-sep {
  background: none !important;
}
.fixed-top_header_fixed {
  position: relative;
}
.menu-width {
  width: 1088px !important;
}
.matrimony-tag-text {
  display: flex;
    margin-top: -15px;
    margin-bottom: 3px;
    color: #000000;
    font-size: 12px;
}
.fixed-topnavbg {
  width: 100%;
    margin: 0px auto;
    background: #fff;
    padding-bottom: 5px;
    padding-top: 13px;
}
.ss-header-nav {
  width: 100%;
    margin: 0px auto;
    background: #fff;
    padding-bottom: 0px;
    padding-top: 0px;
  height: 67px;
}
</style>	<!-- Finger Print JS Load -->
  <script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/UAParser.js?random=110420221510" ></script>
  <script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/fingerprint2.js?random=110420221510" ></script>
  <script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/fingerprint_getid.js?random=110420221510" ></script>
  <!-- Finger Print JS Load End-->
<div id="bmlatestupdate"></div>
<style type="text/css" title="">
#demo-hover a{ background:url(https://imgs.mobileshop.com/bmimgs/hp-tvcommercial.gif) no-repeat; width:57px; height:37px; margin-left:10px; }
#demo-hover a:hover{ background:url(https://imgs.mobileshop.com/bmimgs/hp-tvcommercial-hover.gif) no-repeat;  }
#cboxContent{border-radius:10px;}
</style>
<script>  
if (localStorage.getItem("NEED") === null) 
localStorage.setItem('NEED', 'help');
</script>
<script>

        $(function(){ 
  $('#ID,#MIDP,#MID').bind('input', function(){
    $(this).val(function(_, v){
      return v.replace(/\s+/g, '');
    });
  });
});  

</script>

    <!-- Login Landing Section Start -->
  <div class="container-fluid login-bg-banner-mobileshop" id="resLoginForm">
  <div class="container-fluid custom-container xs-pad0">
    <div class="row">
      <div class="col-md-6 col-12 mt-4 xs-none">
        <!-- <img src="https://imgs.mobileshop.com/bmimgs/login/login-banner-dhoni-bg.png?v1" width="96%"> -->
      </div>
      <!-- Mobile View Start -->
      <div class="col-md-6 col-12 mt-4 md-none xs-login-bg-banner-mobileshop">

        <div class="md-none" style="float: left;width: 100%;margin-top: 8px;margin-bottom: 13px;padding-left: 10px;">
          <div style="float: left;width: width: 50%;">
          <div class="logotop">
          <div class="logotxt" style="color:#777777;font-size: 10px;text-align: left;height: 16px;"></div>
          <div><a href="//www.mobileshop.com"><img width="130" class="bmlogo-width" border="0" title="Mobile Shops" alt="Mobile Shops" src="https://imgs.mobileshop.com/bmimgs/mobileshop-logo.png" itemprop="contentUrl"/></a></div>
          </div>
          </div>
          <div style="float: right;width: 50%;margin-top: 18px;">
          <a href="https://www.mobileshop.com" style="background: transparent;color: #ff9902;text-decoration: none;padding: 7px 13px;border-radius: 7px;font-size: 11px;font-weight: 900;border: 1px solid #ff9902;letter-spacing: 0.7px;margin-right: 10px;float: right;">
          REGISTER FREE</a>
          </div>
        </div>

        <div class="paddt15 xs-login-banner">
        <div class="fleft" style="width: 45%;height: 140px;"> 
        <!-- <img src="//imgs.mobileshop.com/bmimgs/hp-mob-dhonibg.png?v=1" alt="dhoniimage" style="float: left;margin-left: 4px;"/> -->
        &nbsp;
        </div>
        <div class="fleft login-txt-width" >
        <div class="title-tag-txt">Millions of Indians found their perfect match here!</div>
        <div style="font-size: 12px;font-weight:bold;color: #000000;letter-spacing: 0.72px;margin-top: 4px;text-align:left;">You too can find a life partner</div>
        </div>
        <div class="clear"><!----></div>
        </div>
      </div>
      <!-- Mobile View End -->

      <div class="col-md-6 col-12 mt-4 mb-4 xs-pad0 xs-mt0">
        <div class="col-md-12 col-12 login-bg-color xs-pad0">				<div class="col-md-12 col-12 login-title-txt">Existing Member? Login</div>
        <div class="col-md-12 col-12 xs-form-pad">
          <form name="Login"  method="post" action="https://profile.mobileshop.com/login/memlogin.php?" style="margin:0px;">
          <INPUT TYPE='HIDDEN' VALUE='LFR' NAME='dLT' id='dLT'>
          <INPUT TYPE='HIDDEN' VALUE='https://www.mobileshop.com/login/login.php' NAME='dTHR' id='dTHR'>
          <input type='hidden' value='' name='fpDT' id='fpDT'/>
                  <div class="login-label p-0">

          <div class="col-md-12 col-12 float-left pt-0 xs-text-left"><span id="successpop" class="errortxt success-otp" style="padding: 0px;display:block;line-height:20px; font-size:13px;float: left;width: 100%;text-align: left;color:green"></span>

          <span id="errorpop" class="errortxt" style="padding: 0px;display:block;line-height:14px;"></span>

          <label class="xs-label-font md-none fw9" for="STAYLOGIN" id="">Mobile No. / Email ID </label>

          <input  type="text" class="md-input-field input-field" tabindex="1" autocomplete="off" placeholder="Enter Mobile No /    E-Mail ID" autofocus name="MIDP" id="MIDP" value="" onKeyUp="errorclear('MID');"/>
          </div>

          <div class="col-md-12 col-12 float-left pt-3 xs-text-left"> 
          <label class="xs-label-font md-none fw9" for="STAYLOGIN">Password</label> 

          <input type="password" name="PASSWORD2" tabindex="1" autocomplete="off" id="PASSWORD2" class="md-input-field input-field" placeholder="Enter Password" maxlength=20 onKeyUp="errorclear('PASSWORD2');"/>
          <!-- <img onclick="myFunction(this)" src="http://imgs.mobileshop.com/bmimgs/login/login-eye-icon.png" class="login-eye-icon"> -->
          <span onclick="myFunction(this);showHidePwd('PASSWORD2')" class="login-eye-off">
          </span>
          </div>

                      <div class="col-md-12 col-12 float-left text-left pt-4 xs-pt-15" style="display: block;margin-bottom: -15px;">
              <input type="checkbox" class="radiomargin" value="1" name="STYLG" id="STYLG" checked=""> <label class="font-weight-light trouble-txt" for="STYLG" id="">Keep me logged in</label>
            </div>

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15">
            <input type="submit" value="LOGIN" class="login-btn"  onclick="javascript:return chkvalid();" />
          </div>

          <div class="col-md-12 col-12 float-left pt-4 trouble-txt color-initial xs-trouble-txt">
            Trouble logging in?
          </div>
                    <div class="col-md-12 col-12 float-left pt-2 font-weight-light trouble-txt">
            <div class="color-initial"><a href="javascript:void(0);" onclick="otplogin('popotp'); ga('send', 'event','LoginViaOTP-WEB-Mobileshop','Login Via OTP','Link Click'); ga('tracker1.send','event','LoginViaOTP-WEB-Mobileshop','Login Via OTP','Link Click',{'nonInteraction': true});" 
            id="poppwd" class="mr-3 text-decoration-none color-inherit login-normal-txt">Login with OTP</a> <span class="color-grey">|</span> <a href="javascript:void(0);" onclick="forgotpasswd('poppwd');" id="poppwd" class="ml-3 text-decoration-none color-inherit login-normal-txt">Forgot password?</a></div>
          </div>

          </form>
          <div class="clear"><!--  --></div>
                  </div>
      </div>
    </div>
        <div class="col-md-12 col-12 login-bg-color login-mr-txt">
          <div class="row xs-form-pad">
            <span class="cursor-pointer">Not a Member?</span>
            <span class="pl-1 cursor-pointer login-register-txt color-initial"><a href="https://www.mobileshop.com" tabindex="5" class="text-decoration-none color-inherit">Register Free</a></span>
          </div>
        </div>

        <div class="col-md-12 col-12 login-bg-color download-app-padding xs-none">
          <div class="row d-flex align-items-center cursor-pointer download-app-border">
            <div class="col-md-3 col-6 app-img-bottom"><img src="http://imgs.mobileshop.com/bmimgs/login/login-download-app.png?9"></div>
            <div class="col-md-5 col-6 pl-0 pr-0 app-download-txt">
              Get instant updates about your matches! Download our app now!
            </div>
            <div class="col-md-4 col-6">

              <a href="https://www.mobileshop.com/matrimony-mobile-apps" target="_blank" class="color-inherit">
                <div>
                  <div>																					<span><a href="https://market.android.com/details?id=com.mobileshop" target="_blank"><img src="//imgs.mobileshop.com/bmimgs/download-andriod-img.png" border="0" class="mb-1" /></a></span>
                    <span><a href="https://itunes.apple.com/us/app/mobileshop-matrimonial/id465923141?mt=8" target="_blank"><img src="//imgs.mobileshop.com/bmimgs/download-ios-img.png" border="0" /></a></span>

                  </div>
                </div> </a>						</div>
          </div>
        </div>

        <!-- Download Button For Mobile Start -->
        <div class="container-fluid custom-container md-none xs-mb20">
          <div class="row no-gutters">
            <div class="col-lg-12 col-md-12 col-sm-12 col-12 download-mobile">
              <div class="download-text">
                <a href="https://market.android.com/details?id=com.mobileshop" class="color-inherit">
                  <div style="margin-bottom:7px;">Get instant updates about your <br> matches! Download our app now!</div>
                  <div class="download-app-text" style="text-align:center !important;">									<span><img src="//imgs.mobileshop.com/bmimgs/download-andriod-img.png" class="img-fluid"></span>

                  </div>
                </div> </a>							<img src="//imgs.mobileshop.com/bmimgs/seo-mobile-appdownload-bg.jpg" class="img-fluid pr-0">
            </div>
          </div>
        </div>
        <!-- Download Button For Mobile End -->
      </div>
    </div>
  </div>
  </div>
  </div>
  </div>
  <!-- Login Landing Section End -->

  <!-- Login With OTP and Enter OTP Section Start -->
  <div class="container-fluid float-left login-bg-banner" id="resLoginViaOtp" style="display:none;">
  <div class="container-fluid custom-container xs-pad0">
    <div class="row">
      <div class="col-md-6 col-12 mt-4 xs-none">
        <img src="https://imgs.mobileshop.com/bmimgs/login/login-otp-banner.png?v=1" class="ml-4">
      </div>

      <div class="col-md-6 col-12 mt-5 xs-pad0 xs-mt0">
        <!-- Login With OTP Section Start  -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="loginviaotp" style="display: none;">

        <form name="loginviaotpfrm">

        <div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick="loginHideShow('resLoginViaOtp','resLoginForm')"> Login with OTP</div>
        <div class="col-md-12 col-12 xs-form-pad">

        <div class="col-md-12 col-12 xs-banner-margin md-none">
          <img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1">
        </div>

        <div class="login-label">

          <div class="col-md-12 col-12 float-left pt-0 xs-text-left">

          <div class="xs-label-font login-otp-txt xs-mb20">Enter the login detail below and we'll send you an OTP to your registered mobile number</div>

          <span id="errorPopOtpID" class="errortxt" style="padding: 0px;display:block;line-height:14px;float: left;width: 100%;text-align: left;"></span>

          <label class="font-weight-bold xs-label-font login-otp-txt md-none fw9" for="STAYLOGIN" id="">Mobile No / E-mail ID</label>

          <input type="text" class="input-field" id="otploginID" name="otploginID" placeholder="Enter Mobile No. /  Email ID" class="paddl10 mediumtxt1" />

          </div>

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-one">
            <input type="button" value="SUBMIT" class="login-btn" name="otpuserLogin" onClick="javascript:return chkValidOtpID();" />
          </div>

          <div class="clear"><!--  --></div>
        </div>

        </div>
        </form>
        </div>
        <!-- Login With OTP Section End -->

        <!-- Enter OTP Section Start -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="otppageid" style="display: none;">

        <form name="otptologinfrm">	

        <div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick="loginHideShow('otppageid','loginviaotp')"> Enter OTP</div>
        <div class="col-md-12 col-12 xs-form-pad">

        <div class="col-md-12 col-12 xs-banner-margin md-none">
          <img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1">
        </div>

        <div class="login-label">

          <div class="col-md-12 col-12 float-left pt-0 xs-text-left"><span id="errorpop2" class="errortxt success-otp" style="padding: 0px;display:block;line-height:20px; font-size:13px;float: left;width: 100%;text-align: left;"></span>

          <span id="errorpop1" class="errortxt" style="padding: 0px;display:block;line-height:14px;float: left;width: 100%;text-align: left;"></span>


          <div class="xs-label-font login-otp-txt xs-mb20">We've sent you the OTP via SMS to your registered mobile number <span id="otpMobNum"></span>.</div>

          <label class="font-weight-bold xs-label-font login-otp-txt md-none fw9" for="STAYLOGIN" id="">Please enter the OTP you have received</label>

          <input type="text" class="input-field" name="otppin" id="otppin" placeholder="Enter OTP" />
          <input type="hidden" id="otpid" name="otpid" value="" />

          </div>

          <div id="loginViaOtpHide" class="col-md-12 col-12 float-left text-left pt-3 xs-pt-15 color-initial">
            <span class="receieve-txt">Didn't Receive OTP?</span>
            <a href="javascript:resendotp();" class="text-decoration-none response-txt color-inherit">Resend Now</a>
          </div>

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-two">
            <input type="button" value="SUBMIT" name="otppinsubmit" class="login-btn"  onClick="javascript:return chkotpvalid();" />
          </div>

          <div class="clear"><!--  --></div>
        </div>

        </div>
        </form>
        </div>
        <!-- Enter OTP Section End -->

        <!-- Enter OTP SMS & Mail Section Start -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="forgetOtpPageid" style="display: none;">

        <form name="otptologinfrm">

        <div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick="loginHideShow('forgetOtpPageid','forgotpassword')"> Enter OTP</div>
        <div class="col-md-12 col-12 xs-form-pad">

        <div class="col-md-12 col-12 xs-banner-margin md-none">
          <img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1">
        </div>

        <div class="login-label">

          <div class="col-md-12 col-12 float-left pt-0 xs-text-left">

          <span id="forgeterrorpop2" class="errortxt success-otp" style="padding: 0px;display:block;line-height:20px; font-size:13px;float: left;width: 100%;text-align: left;"></span>

          <span id="forgeterrorpop1" class="errortxt" style="padding: 0px;display:block;line-height:14px;float: left;width: 100%;text-align: left;"></span>

          <div class="xs-label-font login-otp-txt xs-mb20">We've sent you the OTP and the link to reset your password via SMS / Email</div>

          <label class="font-weight-bold xs-label-font login-otp-txt md-none fw9" for="STAYLOGIN" id="">Please enter the OTP you have received</label>

          <input type="text" class="input-field" id="forgetotppin" placeholder="Enter OTP"/>
          <input type="hidden" id="fpwdid" name="fpwdid" value="" />

          </div>

          <div id="forgotPwdOtpHide" class="col-md-12 col-12 float-left text-left pt-3 xs-pt-15 color-initial">
            <span class="receieve-txt">Didn't Receive OTP?</span>
            <a href="javascript:forgetResendOtp();" class="text-decoration-none response-txt color-inherit">Resend Now</a>
          </div>

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-two">
            <input type="button" value="SUBMIT" name="otppinsubmit" class="login-btn"  onClick="javascript:return forgetpwdchkotpvalid();" />
          </div>

          <div class="clear"><!--  --></div>
        </div>

        </div>
        </form>
        </div>
        <!-- Enter OTP SMS & Mail Section End -->

        <!-- Forgot Password Section Start -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="forgotpassword" style="display: none;">

        <form name="forgotpasswrdfrm">

        <div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick="loginHideShow('resLoginViaOtp','resLoginForm')"> Forgot password?</div>
        <div class="col-md-12 col-12 xs-form-pad">

        <div class="col-md-12 col-12 xs-banner-margin md-none">
          <img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1">
        </div>

        <div class="login-label">

          <div class="col-md-12 col-12 float-left pt-0 xs-text-left">

          <div class="xs-label-font login-otp-txt xs-mb20">Enter the login detail below and we'll send you a link and OTP to reset your password</div>

          <span id="forgetErrorPop" class="errortxt" style="padding: 0px;display:block;line-height:14px;float: left;width: 100%;text-align: left;"></span>

          <label class="font-weight-bold xs-label-font login-otp-txt md-none fw9" for="STAYLOGIN" id="">Mobile No /  E-Mail ID</label>

          <input type="text" class="input-field" id="forgotpwdid" name="ffpass" placeholder="Enter Mobile No /  E-Mail ID" />

          </div>

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-one">					
            <input type="button" value="SUBMIT" class="login-btn" name="forgotpwd" onClick="javascript:return checkvalid();" />
          </div>

          <div class="clear"><!--  --></div>
        </div>

        </div>
        </form>
        </div>
        <!-- Forgot Password Section End -->

        <!-- Reset Password Section Start -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="newpassword" style="display: none;">

        <form name="newpwdfrm">	

        <div class="col-md-12 col-12 login-title-txt"><span id="newPasswordBackId"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick="loginHideShow('newpassword','forgetOtpPageid')"></span> Reset Password</div>
        <div class="col-md-12 col-12 p-0 xs-form-pad">

        <div class="col-md-12 col-12 xs-banner-margin md-none">
          <img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1">
        </div>

        <div class="login-label">

          <div class="col-md-12 col-12 float-left pt-0 xs-pad0 xs-text-left">

          <span id="errorpop3" class="errortxt" style="padding: 3px;display:block;line-height:14px;font-size: 12px;    margin-bottom: -10px;padding-left: 14px;"></span>

          <span id="errorpop4" class="errortxt" style="padding: 3px;display:block;line-height:14px;font-size: 12px;    margin-bottom: -10px;padding-left: 14px;"></span>

          <div class="col-md-12 col-12 float-left pt-3 xs-text-left"> 
          <label class="xs-label-font md-none fw9" for="STAYLOGIN">New Password</label> 

          <input type="password" class="input-field" id="newpass" name="newpass" placeholder="Enter New Password" />				
          <span onclick="myFunction(this);showHidePwd('newpass')" class="login-eye-off">
          </span>
          </div>

          <div class="col-md-12 col-12 float-left pt-3 xs-text-left"> 
          <label class="xs-label-font md-none fw9" for="STAYLOGIN">Confirm Password</label> 

          <input type="password" class="input-field" id="confpass" name="confpass" placeholder="Enter Confirm Password" />
          <input type="hidden" name="matriid" id="matriid" value="" />
          <input type="hidden" name="redispwd" id="redispwd" value="" />
          <span onclick="myFunction(this);showHidePwd('confpass')" class="login-eye-off">
          </span>

          </div> 

          <div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-two">
            <input type="button" value="RESET PASSWORD" class="login-btn" name="newpwdsubmit" onClick="javascript:return chknewpwd();" />
          </div>
          </div>
          <div class="clear"><!--  --></div>
        </div>

        </div>
        </form>
        </div>
        <!-- Reset Password Section End -->
        <!-- Multi id Section Start -->
        <div class="col-md-12 col-12 login-bg-color xs-pad0" id="multiids" style="display: none;">
        </div>
        <!-- Multi id Section End -->
      </div>
    </div>
  </div>
  </div>
  <!-- Login With OTP and Enter OTP Section End -->

  <div class="container-fluid moz-pad0">
  <div class="container-fluid p-0">
  <div class="row three-dots-moz" id="mobileFooter">
    <div class="col-md-12 col-12 p-0">
      <div class="frmbtn-icn"> 
      <div class="innerwrapper">
      <div class="fleft txt-left frmbtn-icn1">
      <div class="fleft paddt10">
      <img alt="Contact genuine profiles" class="lazyloaded xs-none" src="//imgs.mobileshop.com/bmimgs/login/seo-desk-footer-icon-1.png?v1">

      <img src="//imgs.mobileshop.com/bmimgs/login/seo-mob-footer-icon-1.svg" alt="Contact genuine profiles" class="md-none">

      </div>
      <div class="fleft hp-lheight21 hppaddl20 frmbtmwidth1"> Contact genuine profiles with  100% verified mobile numbers </div>
      </div>
      <div class="fleft txt-left frmbtn-icn2">
      <div class="fleft paddt10">
      <img alt="Highest number of  documented marriages" class="lazyloaded xs-none" src="//imgs.mobileshop.com/bmimgs/login/seo-desk-footer-icon-2.png?v1" class="xs-none">

      <img src="//imgs.mobileshop.com/bmimgs/login/seo-mob-footer-icon-2.svg" alt="Highest number of  documented marriages" class="md-none">

      </div>
      <div class="fleft hp-lheight21 hppaddl20 frmbtmwidth2"> Highest number of  documented marriages online <div style="font-size:12px;font-weight:400;" class="paddt5"> - Limca Book of Records</div></div>
      </div>
      <div class="fleft txt-left frmbtn-icn3">
      <div class="fleft paddt10"> <img alt="The most trusted matrimony brand" class="lazyloaded xs-none" src="//imgs.mobileshop.com/bmimgs/login/seo-desk-footer-icon-3.png?v1" class="xs-none"> 

      <img src="//imgs.mobileshop.com/bmimgs/login/seo-mob-footer-icon-3.svg" alt="The most trusted matrimony brand" class="md-none">

      </div>
      <div class="fleft hp-lheight21 hppaddl20 frmbtmwidth3"> The most trusted matrimony brand <div style="font-size:12px;font-weight:400;" class="paddt5"> - The Brand Trust Report</div></div>
      </div>
      <div class="clear"><!----></div>
      </div>				
      </div>
    </div>
  </div>
  </div>
  </div>

  <div class="wrapper-max paddt20" style="display:none;">
  <table border="0" cellpadding="0" cellspacing="0">
  <tr>
  <td valign="top" onclick="regPDLogTrackAjax('Loginpage-part')">
    <div id="rndcorner" style="width:450px;border-top-left-radius:10px;border-top-right-radius:10px; border:1px solid #d9d9d9; display:block;" class="txt-left">
      <div style="padding:15px 25px;border-top-left-radius:10px;border-top-right-radius:10px;" class="hdtittle">Member Login</div>
            <div class="paddb20 paddl25">
        <form name="Login"  method="post" action="https://profile.mobileshop.com/login/memlogin.php?" style="margin:0px;">
        <INPUT TYPE='HIDDEN' VALUE='LFR' NAME='dLT' id='dLT'>
        <INPUT TYPE='HIDDEN' VALUE='https://www.mobileshop.com/login/login.php' NAME='dTHR' id='dTHR'>
        <input type='hidden' value='' name='fpDT' id='fpDT'/>
        <div style="width:400px;">
          <div class=" paddt5"><span id="errorpop" class="errortxt" style="padding: 0px;display:block;line-height:14px;"></span><label class="radiolabel hdtxt lheight120 boldtxt txtopac" for="STAYLOGIN" style="color:#323232;" id="">Mobile No. / Matrimony ID / Email ID </label>
          <input type="text" class="paddl10 mediumtxt1" tabindex="1" autocomplete="off" style="width:97%;height:35px;border:1px solid #b2b2b2;padding-top:8px\9;height:30px\9;" autofocus name="MIDP" id="MIDP" value="" onKeyUp="errorclear('MID');"/></div>
          <div class=" paddt10"> <label class="radiolabel hdtxt lheight120 boldtxt txtopac" for="STAYLOGIN" style="color:#323232;">Password</label>
          <input type="password" name="PASSWORD2" tabindex="1" autocomplete="off" id="PASSWORD2" class="paddl10 mediumtxt1" style="width:97%;height:35px;border:1px solid #b2b2b2;padding-top:8px\9;height:30px\9;" maxlength=20 onKeyUp="errorclear('PASSWORD2');"/></div>
          <div class="fleft paddt10 hdtxt txtopac"><a href="javascript:void(0);" onclick="forgotpasswd('poppwd');" id="poppwd" class="utxt">Forgot Password?</a> |<a href="javascript:void(0);" onclick="otplogin('popotp'); ga('send', 'event','LoginViaOTP-WEB-Mobileshop','Login Via OTP','Link Click'); ga('tracker1.send','event','LoginViaOTP-WEB-Mobileshop','Login Via OTP','Link Click',{'nonInteraction': true});" 
            id="poppwd" class="utxt" style="margin-left:7px;">Login Via OTP</a><br /><div id="" class="paddt8" style="display: block;"><input type="checkbox" class="radiomargin" value="1" name="STYLG" id="STYLG" style="margin:0px;" checked=""> <label class="radiolabel clr7 mediumtxt1" for="STYLG" style="color:#777777; " id="">Keep me logged in</label></div></div>
          <div class="fright paddt15 hdtxt txtopac"><input type="submit" value="LOGIN" style="background:#ff7c0b;border-radius:2px;text-decoration:none;display:block;border:1px solid #ff7c0b;" class="hdtxt1 boldtxt clr6 paddt5 paddr15 paddb5 paddl15"  onclick="javascript:return chkvalid();" /></div>
          </form>
          <div class="clear"><!--  --></div>
                  </div>
      </div>
  </div>

              <div style="width:450px;" class="txt-left paddt10">
          <div style="padding: 8px 2px 0px 0px;display:block;" id="regfree" class="mediumtxt">Not a member yet? <a href="https://www.mobileshop.com" tabindex="5">Click here</a> to register.</div>	
        </div>
        </td>
  <td valign="top"><link rel="stylesheet" type="text/css" href="https://imgs.mobileshop.com/bmstyles/mini/commonmini040620190000.css" />
<link rel="stylesheet" type="text/css" href="https://imgs.mobileshop.com/bmstyles/form.css" />
<script language=javascript src="https://imgs.mobileshop.com/scripts/jquery.js?random=110420221510"></script>
<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/common.js?random=110420221510" ></script>
<script type="text/javascript" language="javascript" src="https://imgs.mobileshop.com/scripts/headerjs.js?random=110420221510" ></script>
<script language=javascript src="https://imgs.mobileshop.com/scripts/register-form-check.js?random=110420221510"></script>

<script language=javascript src="https://imgs.mobileshop.com/scripts/colorbox.js?random=110420221510"></script>

<script language=javascript src="https://imgs.mobileshop.com/scripts/retailoutlets.js?random=110420221510"></script>
<script type="text/javascript" src="https://imgs.mobileshop.com/scripts/reggatrack.js?random=110420221510">
</script>
<style>
.login-pop-div {
    position: absolute;
    top: -45px;
    z-index: 1;
}
.inputtext {
  border:1px solid #d1d1d1;
  color: #666666;
  font-family: arial,verdana;
  padding: 4px;
}

.profile-secure-icon{
  display: inline-block;
    padding-left: 25px;
  padding-top:5px;
  background:url("https://imgs.mobileshop.com/bmimgs/visitpop-prof-lock-icon.gif") no-repeat scroll 0 0 transparent;
  height:22px;
}
</style>
<script language="javascript">
  function close_popup(){
    document.cookie="VISITORPOPUP=1;path=/";
    parent.document.getElementById("top_block").style.display="none"
    parent.document.getElementById("overlay").style.display="none"
  }
</script>

<div id="rndcorner" style="width:450px;border-top-left-radius:10px;border-top-right-radius:10px; border:1px solid #d9d9d9; display:block;margin-left:50px;" class="txt-left">
  <div style="padding:15px 25px;border-top-left-radius:10px;border-top-right-radius:10px;" class="hdtittle">Not a Member? Register Free</div>
      <!-- Form Starts -->	



<style>
#hpregform-new { margin:5px 0 0 !important;} #hpregform-new dt { width:165px; } #hpregform-new dd {margin:7px 0px;} #hpregform-new dl {clear: both; display: block; font: bold 12px arial,verdana; height: 25px !important; margin: 0; padding: 2px 0 1px !important;} #hpregform-new dt label { line-height:30px;}

.hp-regform-txtfield-new{border:1px solid #e0e0e0; background:#fff; color:#777777; width:230px; padding-left:10px; height:27px; font:12px arial; *padding-top:5px; *height:20px;}
.ie8 .hp-regform-txtfield-new{border:1px solid #e0e0e0; background:#fff; color:#777777; width:230px; padding-left:10px; font:12px arial; padding-top:5px; height:20px;}
.hp-regform-bg1 #hp-regform-new1 dl{color:#363636;}
#hp-regform-new1 select,#quicksearchform1 select{background: #ffffff; color:#777; border:1px solid #e0e0e0; display: inline-block;  -webkit-appearance:none;  -moz-appearance:none;  appearance:none; cursor:pointer; height:28px; padding:5px;}
#hp-regform-new1 dt{float:left;padding-top:5px;width:140px}#hp-regform-new1 dl{clear:both;display:block;font:14px arial,verdana;height:32px;margin:0;padding:3px 0 2px}#hp-regform-new1 dd{float:left;font:12px arial,verdana;margin-bottom:1px!important}
.hp-mobile-icon-new{background:url(https://imgs.mobileshop.com/bmimgs/hp-mobile-white-icon.png) no-repeat; padding-left:55px; padding-right:25px; margin-right:25px;border-right:1px solid #ffffff;* filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='https://imgs.mobileshop.com/bmimgs/hp-mobile-icon.png', sizingMethod='crop');* background:none!important}.hp-hand-icon-new{background:url(https://imgs.mobileshop.com/bmimgs/hp-most-trust-white-icon.png) no-repeat; padding-right:50px; padding-left:70px;padding-right:25px; margin-right:25px;border-right:1px solid #ffffff;* filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='https://imgs.mobileshop.com/bmimgs/hp-most-trust-icon.png', sizingMethod='crop');* background:none!important}.hp-awards-icon-new{background:url(https://imgs.mobileshop.com/bmimgs/hp-awards-white-icon.png) no-repeat;padding-left:74px;* filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='https://imgs.mobileshop.com/bmimgs/hp-awards-icon.png', sizingMethod='crop');* background:none!important}.hp-awards-icon-new,.hp-hand-icon-new,.hp-mobile-icon-new{display:inline-block;font:700 15px/20px arial;-moz-font-smoothing:antialiased;-webkit-font-smoothing:antialiased;letter-spacing:0;color:#FFF;text-shadow:1px 1px 1px #000}
.hp-regformbg1-txt{font:italic 19px/24px georgia;color:#363636;font-smooth:1em;margin-left:0}
.hp-regform-bg1 #hp-regform-new dl{color:#777;}
#hp-regform-new select,#quicksearchform select{background: #ffffff; color:#777; border:1px solid #e0e0e0; display: inline-block;  -webkit-appearance:none;  -moz-appearance:none;  appearance:none; cursor:pointer; height:28px; padding:5px;}
#quicksearchform select{height:35px;}
.select-arw{position:relative}#quicksearchform .select-arw:after,.select-arw:after{content:" ";border-top:7px solid #a3a5a5;border-left:4px solid transparent;border-right:4px solid transparent;right:6px;top:12px;padding:0;position:absolute;pointer-events:none;}#quicksearchform .select-arw:before,.select-arw:before{content:'';right:1px;top:1px;width:22px;height:26px;background:#fff;position:absolute;pointer-events:none;display:block}#quicksearchform .select-arw:before{height:33px;width:25px}#quicksearchform .select-arw:after{top:15px;right:10px}#hp-regform-new dt{float:left;padding-top:5px;width:161px}#hp-regform-new dl{clear:both;display:block;font:700 14px arial,verdana;height:32px;margin:0;padding:3px 0 2px}#hp-regform-new dd{float:left;font:12px arial,verdana;margin-bottom:1px!important}
</style>

<!-- enquiry box right -->
<div class="paddt10">				
  <div style=" width:420px;">


  <!-- Register Form - Start -->
    <form target="_parent" method="post" action="https://secure.mobileshop.com/register/regredirect.php" name="registrationform" onsubmit="return validateregistrationform();" style="margin:0px;"> 
      <div id="hp-regform-new1" class="mediumtxt" style="padding-left:15px;"> 
        <dl>
          <dt><label for="REGISTERED_BY">Profile for</label></dt>
          <dd class="select-arw">
            <select name="REGISTERED_BY" id="REGISTERED_BY" style="width:240px;" onchange="show_genfun();agesel();gentrack();registrationform.NAME.focus();">
            <option value="0">-Select-</option>
            <option value="1">Myself</option><option value="8">Son</option><option value="9">Daughter</option><option value="10">Brother</option><option value="11">Sister</option><option value="4">Relative</option><option value="5">Friend</option>						</select>
          </dd>
        </dl>

        <dl>
          <dt><label for="NAME"><span id="mpname">Name</span></label></dt>
          <dd><input type="text" name="NAME" id="NAME" style="width:230px;" maxlength="40" class="hp-regform-txtfield-new" value=""></dd>
        </dl> 

        <dl style="height:25px;padding-top:5px;">
          <dt style="padding-top:0px;"><label for="gendermale">Gender</label></dt>
          <dd>
            <label for="gendermale">
            <input type="radio" style="vertical-align:middle; display:inline; float:none; margin:0px 2px 0px 3px; _margin:0px 1px 0px 1px;" value="M" name="GENDER" id="gendermale" onclick="javascript:loadDOByear();var val=0; val = RegGATrack($(this).val(),'Sregform-male',$('#gatrack-gender-m-count').val(),1);if(val==1){$('#gatrack-gender-m-count').val(1);}" class="hp-gender"> Male
            </label>

            <label for="genderfemale">
            <input type="radio" style="vertical-align:middle; display:inline; float:none; margin:0px 2px 0px 3px; _margin:0px 1px 0px 1px;" value="F" name="GENDER" id="genderfemale" onclick="javascript:loadDOByear();var val=0; val = RegGATrack($(this).val(),'Sregform-female',$('#gatrack-gender-f-count').val(),1);if(val==1){$('#gatrack-gender-f-count').val(1);} " class="hp-gender"> Female
            </label>
            <input type="hidden" name="GEN_VAL" id="GEN_VAL" value="">
          </dd>
        </dl> 

        <dl style="height:22px;">
          <dt><label for="DOBDAY"><span id="mpage">Date of Birth</span></label></dt>
          <dd id="DOBBOX">
            <div class="fleft paddr2">
              <div class="fleft select-arw">
              <select name="DOBDAY" id="DOBDAY" style="width:75px;" onchange="agesel(); ">
                <option value="0" selected="">DD</option>
                <option value="1" >1</option><option value="2" >2</option><option value="3" >3</option><option value="4" >4</option><option value="5" >5</option><option value="6" >6</option><option value="7" >7</option><option value="8" >8</option><option value="9" >9</option><option value="10" >10</option><option value="11" >11</option><option value="12" >12</option><option value="13" >13</option><option value="14" >14</option><option value="15" >15</option><option value="16" >16</option><option value="17" >17</option><option value="18" >18</option><option value="19" >19</option><option value="20" >20</option><option value="21" >21</option><option value="22" >22</option><option value="23" >23</option><option value="24" >24</option><option value="25" >25</option><option value="26" >26</option><option value="27" >27</option><option value="28" >28</option><option value="29" >29</option><option value="30" >30</option><option value="31" >31</option>							</select>
              </div>
              <div class="fleft select-arw paddl10">	
              <select style="width:75px;" name="DOBMONTH" id="DOBMONTH" size="1" onchange="updateDay('month','registrationform','DOBYEAR','DOBMONTH','DOBDAY'); agesel()">
                <option value="0" selected="">MM</option>
                <option value="1" >Jan</option><option value="2" >Feb</option><option value="3" >Mar</option><option value="4" >Apr</option><option value="5" >May</option><option value="6" >Jun</option><option value="7" >Jul</option><option value="8" >Aug</option><option value="9" >Sep</option><option value="10" >Oct</option><option value="11" >Nov</option><option value="12" >Dec</option>							</select>	
              </div>
              <div class="fleft select-arw paddl10">
              <select name="DOBYEAR" id="DOBYEAR" style="width:70px;" onchange="updateDay('year','registrationform','DOBYEAR','DOBMONTH','DOBDAY'); agesel();">
                <option value="0" selected="">YYYY</option>
                <option value="2007" >2007</option><option value="2006" >2006</option><option value="2005" >2005</option><option value="2004" >2004</option><option value="2003" >2003</option><option value="2002" >2002</option><option value="2001" >2001</option><option value="2000" >2000</option><option value="1999" >1999</option><option value="1998" >1998</option><option value="1997" >1997</option><option value="1996" >1996</option><option value="1995" >1995</option><option value="1994" >1994</option><option value="1993" >1993</option><option value="1992" >1992</option><option value="1991" >1991</option><option value="1990" >1990</option><option value="1989" >1989</option><option value="1988" >1988</option><option value="1987" >1987</option><option value="1986" >1986</option><option value="1985" >1985</option><option value="1984" >1984</option><option value="1983" >1983</option><option value="1982" >1982</option><option value="1981" >1981</option><option value="1980" >1980</option><option value="1979" >1979</option><option value="1978" >1978</option><option value="1977" >1977</option><option value="1976" >1976</option><option value="1975" >1975</option><option value="1974" >1974</option><option value="1973" >1973</option><option value="1972" >1972</option><option value="1971" >1971</option><option value="1970" >1970</option><option value="1969" >1969</option><option value="1968" >1968</option><option value="1967" >1967</option><option value="1966" >1966</option><option value="1965" >1965</option><option value="1964" >1964</option><option value="1963" >1963</option><option value="1962" >1962</option><option value="1961" >1961</option><option value="1960" >1960</option><option value="1959" >1959</option><option value="1958" >1958</option><option value="1957" >1957</option><option value="1956" >1956</option><option value="1955" >1955</option>							</select>
              </div>
            </div> 

            <div style="display: none;" class="fleft" id="ageblock">
            <input type="hidden" name="AGE" id="AGE" size="2" maxlength="2" value=""></div>
          </dd>

          <input type="hidden" id="todayYear" value="2025" name="todayYear">
          <input type="hidden" id="todayMonth" value="07" name="todayMonth">
          <input type="hidden" id="todayDay" value="30" name="todayDay">
        </dl>

        <dl style="padding-top:10px;">
          <dt><label for="RELIGION">Religion</label></dt>
          <dd class="select-arw">
            <select name="RELIGION" id="RELIGION" size="1" style="width:240px;" onchange="document.registrationform.MOTHERTONGUE.selectedIndex=0;">
              <option value="0" selected="">-Select-</option>
              <option value="1">Hindu</option><option value="10">Muslim - Shia</option><option value="11">Muslim - Sunni</option><option value="2">Muslim - Others</option><option value="3">Christian</option><option value="4">Sikh</option><option value="15">Jain - Digambar</option><option value="16">Jain - Shwetambar</option><option value="5">Jain - Others</option><option value="6">Parsi</option><option value="7">Buddhist</option><option value="17">Jewish</option><option value="8">Inter-Religion</option>						</select>
          </dd>
        </dl> 

        <dl>
          <dt><label for="MOTHERTONGUE">Mother Tongue</label></dt>
          <dd class="select-arw">
            <select name="MOTHERTONGUE" id="MOTHERTONGUE" size="1" style="width:240px;" onchange="makeDrequest(this.value);">
              <option value="0"> - Select - </option>
              <option value="54">Angika</option><option value="1">Arunachali</option><option value="2">Assamese</option><option value="3">Awadhi</option><option value="4">Bengali</option><option value="5">Bhojpuri</option><option value="6">Brij</option><option value="7">Bihari</option><option value="53">Badaga</option><option value="8">Chatisgarhi</option><option value="9">Dogri</option><option value="10">English</option><option value="11">French</option><option value="12">Garhwali</option><option value="13">Garo</option><option value="14">Gujarati</option><option value="15">Haryanvi</option><option value="16">Himachali/Pahari</option><option value="17">Hindi</option><option value="18">Kanauji</option><option value="19">Kannada</option><option value="20">Kashmiri</option><option value="21">Khandesi</option><option value="22">Khasi</option><option value="23">Konkani</option><option value="24">Koshali</option><option value="25">Kumaoni</option><option value="26">Kutchi</option><option value="27">Lepcha</option><option value="28">Ladacki</option><option value="29">Magahi</option><option value="30">Maithili</option><option value="31">Malayalam</option><option value="32">Manipuri</option><option value="33">Marathi</option><option value="34">Marwari</option><option value="35">Miji</option><option value="36">Mizo</option><option value="37">Monpa</option><option value="38">Nicobarese</option><option value="39">Nepali</option><option value="40">Oriya</option><option value="41">Punjabi</option><option value="42">Rajasthani</option><option value="43">Sanskrit</option><option value="44">Santhali</option><option value="45">Sindhi</option><option value="46">Sourashtra</option><option value="47">Tamil</option><option value="48">Telugu</option><option value="49">Tripuri</option><option value="50">Tulu</option><option value="51">Urdu</option>						</select>
          </dd>
        </dl> 

        <dl>
          <dt><label for="CASTE_NORMAL">Caste / Division</label></dt>
          <dd class="select-arw">
            <div class="fleft">
              <select style="width:240px;" name="CASTE_NORMAL" id="CASTE_NORMAL" size="1" onchange="showMoreCaste(this.value);">
                <option value="casteselect0" selected="">-Select-</option>
              </select>
            </div>

            <div class="fleft" style="width:105px; display:none; padding-left:3px;" id="spnFreeTxt">
              <input type="text" name="CASTE_FREETEXT" id="CASTE_FREETEXT" class="textfield" size="20" value="- Enter caste -" onfocus="if(this.value=='- Enter caste -') {this.value=''; }" onblur="if(this.value=='') {this.value = '- Enter caste -'; }">
            </div>
            <span id="CASTE_LOADING"></span>
          </dd>
        </dl>					

<script>
function getcntrval()
{
  var getcntrvalindex=document.registrationform.M_COUNTRYCODE.selectedIndex;
  var getcntrval=document.registrationform.M_COUNTRYCODE.options[getcntrvalindex].value;
  document.getElementById('COUNTRY').value = getcntrval;
  setMaxLenMob();
}

setTimeout(function(){ setMaxLenMob(); }, 2000);

function setMaxLenMob()
{
  var getcntrvalindex=document.registrationform.M_COUNTRYCODE.selectedIndex;
  var getcntrval=document.registrationform.M_COUNTRYCODE.options[getcntrvalindex].value;
  if(getcntrval == 98)
    $("#MOBILENO").attr("maxlength", 10)
  else
    $("#MOBILENO").attr("maxlength", 20)
}
</script>


        <dl>
          <dt><label for="M_COUNTRYCODE">Mobile Number</label></dt>
          <dd id="MOBILEBOX">
          <div  class="fleft select-arw">
            <select style="width: 95px;" name="M_COUNTRYCODE" id="M_COUNTRYCODE" class="inputtext" onchange="onTtip(this.value);getcntrval();">
              <option style="" value="98">India (+91)</option><option style="" value="222">United States of America (+1)</option><option style="" value="220">United Arab Emirates (+971)</option><option style="" value="129">Malaysia (+60)</option><option style="" value="221">United Kingdom (+44)</option><option style="" value="13">Australia (+61)</option><option style="" value="185">Saudi Arabia (+966)</option><option style="" value="39">Canada (+1)</option><option style="" value="189">Singapore (+65)</option><option style="" value="114">Kuwait (+965)</option><optgroup label="-------------------------"></optgroup><option style="" value="1">Afghanistan (+93)</option><option style="" value="2">Albania (+355)</option><option style="" value="3">Algeria (+213)</option><option style="" value="4">American Samoa (+684)</option><option style="" value="5">Andorra (+376)</option><option style="" value="6">Angola (+244)</option><option style="" value="7">Anguilla (+1)</option><option style="" value="8">Antarctica (+672)</option><option style="" value="9">Antigua and Barbuda (+1)</option><option style="" value="10">Argentina (+54)</option><option style="" value="11">Armenia (+374)</option><option style="" value="12">Aruba (+297)</option><option style="" value="13">Australia (+61)</option><option style="" value="14">Austria (+43)</option><option style="" value="15">Azerbaijan (+994)</option><option style="" value="16">Bahamas (+1)</option><option style="" value="17">Bahrain (+973)</option><option style="" value="18">Bangladesh (+880)</option><option style="" value="19">Barbados (+1)</option><option style="" value="20">Belarus (+375)</option><option style="" value="21">Belgium (+32)</option><option style="" value="22">Belize (+501)</option><option style="" value="23">Benin (+229)</option><option style="" value="24">Bermuda (+1)</option><option style="" value="25">Bhutan (+975)</option><option style="" value="26">Bolivia (+591)</option><option style="" value="27">Bosnia and Herzegovina (+387)</option><option style="" value="28">Botswana (+267)</option><option style="" value="29">Bouvet Island (+55)</option><option style="" value="30">Brazil (+55)</option><option style="" value="31">British Indian Ocean Territory (+246)</option><option style="" value="32">British Virgin Islands (+1)</option><option style="" value="33">Brunei (+673)</option><option style="" value="34">Bulgaria (+359)</option><option style="" value="35">Burkina Faso (+226)</option><option style="" value="36">Burundi (+257)</option><option style="" value="37">Cambodia (+855)</option><option style="" value="38">Cameroon (+237)</option><option style="" value="39">Canada (+1)</option><option style="" value="40">Cape Verde (+238)</option><option style="" value="41">Cayman Islands (+1)</option><option style="" value="42">Central African Republic (+236)</option><option style="" value="43">Chad (+235)</option><option style="" value="44">Chile (+56)</option><option style="" value="45">China (+86)</option><option style="" value="46">Christmas Island (+672)</option><option style="" value="47">Cocos Islands (+672)</option><option style="" value="48">Colombia (+57)</option><option style="" value="49">Comoros (+269)</option><option style="" value="50">Congo (+242)</option><option style="" value="51">Cook Islands (+682)</option><option style="" value="52">Costa Rica (+506)</option><option style="" value="53">Croatia (+385)</option><option style="" value="54">Cuba (+53)</option><option style="" value="55">Cyprus (+357)</option><option style="" value="56">Czech Republic (+420)</option><option style="" value="57">Denmark (+45)</option><option style="" value="58">Djibouti (+253)</option><option style="" value="59">Dominica (+1)</option><option style="" value="60">Dominican Republic (+1)</option><option style="" value="61">East Timor (+670)</option><option style="" value="62">Ecuador (+593)</option><option style="" value="63">Egypt (+20)</option><option style="" value="64">El Salvador (+503)</option><option style="" value="65">Equatorial Guinea (+240)</option><option style="" value="66">Eritrea (+291)</option><option style="" value="67">Estonia (+372)</option><option style="" value="68">Ethiopia (+251)</option><option style="" value="69">Falkland Islands (+500)</option><option style="" value="70">Faroe Islands (+298)</option><option style="" value="71">Fiji (+679)</option><option style="" value="72">Finland (+358)</option><option style="" value="73">France (+33)</option><option style="" value="74">French Guiana (+594)</option><option style="" value="75">French Polynesia (+689)</option><option style="" value="76">French Southern Territories (+262)</option><option style="" value="77">Gabon (+241)</option><option style="" value="78">Gambia (+220)</option><option style="" value="79">Georgia (+995)</option><option style="" value="80">Germany (+49)</option><option style="" value="81">Ghana (+233)</option><option style="" value="82">Gibraltar (+350)</option><option style="" value="83">Greece (+30)</option><option style="" value="84">Greenland (+299)</option><option style="" value="85">Grenada (+1)</option><option style="" value="86">Guadeloupe (+590)</option><option style="" value="87">Guam (+1)</option><option style="" value="88">Guatemala (+502)</option><option style="" value="89">Guinea (+224)</option><option style="" value="90">Guinea-Bissau (+245)</option><option style="" value="91">Guyana (+592)</option><option style="" value="92">Haiti (+509)</option><option style="" value="93">Heard and McDonald Islands (+672)</option><option style="" value="94">Honduras (+504)</option><option style="" value="95">Hong Kong (+852)</option><option style="" value="96">Hungary (+36)</option><option style="" value="97">Iceland (+354)</option><option style="" value="98">India (+91)</option><option style="" value="99">Indonesia (+62)</option><option style="" value="100">Iran (+98)</option><option style="" value="101">Iraq (+964)</option><option style="" value="102">Ireland (+353)</option><option style="" value="103">Israel (+972)</option><option style="" value="104">Italy (+39)</option><option style="" value="105">Ivory Coast (+225)</option><option style="" value="106">Jamaica (+1)</option><option style="" value="107">Japan (+81)</option><option style="" value="108">Jordan (+962)</option><option style="" value="109">Kazakhstan (+7)</option><option style="" value="110">Kenya (+254)</option><option style="" value="111">Kiribati (+686)</option><option style="" value="112">Korea, North (+850)</option><option style="" value="113">Korea, South (+82)</option><option style="" value="114">Kuwait (+965)</option><option style="" value="115">Kyrgyzstan (+996)</option><option style="" value="116">Laos (+856)</option><option style="" value="117">Latvia (+371)</option><option style="" value="118">Lebanon (+961)</option><option style="" value="119">Lesotho (+266)</option><option style="" value="120">Liberia (+231)</option><option style="" value="121">Libya (+218)</option><option style="" value="122">Liechtenstein (+423)</option><option style="" value="123">Lithuania (+370)</option><option style="" value="124">Luxembourg (+352)</option><option style="" value="125">Macau (+853)</option><option style="" value="126">Macedonia (+389)</option><option style="" value="127">Madagascar (+261)</option><option style="" value="128">Malawi (+265)</option><option style="" value="129">Malaysia (+60)</option><option style="" value="130">Maldives (+960)</option><option style="" value="131">Mali (+223)</option><option style="" value="132">Malta (+356)</option><option style="" value="133">Marshall Islands (+692)</option><option style="" value="134">Martinique (+596)</option><option style="" value="135">Mauritania (+222)</option><option style="" value="136">Mauritius (+230)</option><option style="" value="137">Mayotte (+269)</option><option style="" value="138">Mexico (+52)</option><option style="" value="139">Micronesia, Federated States of (+691)</option><option style="" value="140">Moldova (+373)</option><option style="" value="141">Monaco (+377)</option><option style="" value="142">Mongolia (+976)</option><option style="" value="143">Montserrat (+1)</option><option style="" value="144">Morocco (+212)</option><option style="" value="145">Mozambique (+258)</option><option style="" value="146">Myanmar (+95)</option><option style="" value="147">Namibia (+264)</option><option style="" value="148">Nauru (+674)</option><option style="" value="149">Nepal (+977)</option><option style="" value="150">Netherlands (+31)</option><option style="" value="151">Netherlands Antilles (+599)</option><option style="" value="152">New Caledonia (+687)</option><option style="" value="153">New Zealand (+64)</option><option style="" value="154">Nicaragua (+505)</option><option style="" value="155">Niger (+227)</option><option style="" value="156">Nigeria (+234)</option><option style="" value="157">Niue (+683)</option><option style="" value="158">Norfolk Island (+672)</option><option style="" value="159">Northern Mariana Islands (+1)</option><option style="" value="160">Norway (+47)</option><option style="" value="161">Oman (+968)</option><option style="" value="162">Pakistan (+92)</option><option style="" value="163">Palau (+680)</option><option style="" value="164">Panama (+507)</option><option style="" value="165">Papua New Guinea (+675)</option><option style="" value="166">Paraguay (+595)</option><option style="" value="167">Peru (+51)</option><option style="" value="168">Philippines (+63)</option><option style="" value="169">Pitcairn Island (+64)</option><option style="" value="170">Poland (+48)</option><option style="" value="171">Portugal (+351)</option><option style="" value="172">Puerto Rico (+1)</option><option style="" value="173">Qatar (+974)</option><option style="" value="174">Reunion (+262)</option><option style="" value="175">Romania (+40)</option><option style="" value="176">Russia (+7)</option><option style="" value="177">Rwanda (+250)</option><option style="" value="178">S. Georgia and S. Sandwich Isls. (+500)</option><option style="" value="179">Saint Kitts & Nevis (+1)</option><option style="" value="180">Saint Lucia (+1)</option><option style="" value="181">Saint Vincent and The Grenadines (+1)</option><option style="" value="182">Samoa (+685)</option><option style="" value="183">San Marino (+378)</option><option style="" value="184">Sao Tome and Principe (+239)</option><option style="" value="185">Saudi Arabia (+966)</option><option style="" value="186">Senegal (+221)</option><option style="" value="187">Seychelles (+248)</option><option style="" value="188">Sierra Leone (+232)</option><option style="" value="189">Singapore (+65)</option><option style="" value="190">Slovakia (+421)</option><option style="" value="191">Slovenia (+386)</option><option style="" value="192">Somalia (+252)</option><option style="" value="193">South Africa (+27)</option><option style="" value="194">Spain (+34)</option><option style="" value="195">Sri Lanka (+94)</option><option style="" value="196">St. Helena (+290)</option><option style="" value="197">St. Pierre and Miquelon (+508)</option><option style="" value="198">Sudan (+249)</option><option style="" value="199">Suriname (+597)</option><option style="" value="200">Svalbard and Jan Mayen Islands (+47)</option><option style="" value="201">Swaziland (+268)</option><option style="" value="202">Sweden (+46)</option><option style="" value="203">Switzerland (+41)</option><option style="" value="204">Syria (+963)</option><option style="" value="205">Taiwan (+886)</option><option style="" value="206">Tajikistan (+992)</option><option style="" value="207">Tanzania (+255)</option><option style="" value="208">Thailand (+66)</option><option style="" value="209">Togo (+228)</option><option style="" value="210">Tokelau (+690)</option><option style="" value="211">Tonga (+676)</option><option style="" value="212">Trinidad and Tobago (+1)</option><option style="" value="213">Tunisia (+216)</option><option style="" value="214">Turkey (+90)</option><option style="" value="215">Turkmenistan (+993)</option><option style="" value="216">Turks and Caicos Islands (+1)</option><option style="" value="217">Tuvalu (+688)</option><option style="" value="218">Uganda (+256)</option><option style="" value="219">Ukraine (+380)</option><option style="" value="220">United Arab Emirates (+971)</option><option style="" value="221">United Kingdom (+44)</option><option style="" value="222">United States of America (+1)</option><option style="" value="223">Uruguay (+598)</option><option style="" value="224">Uzbekistan (+998)</option><option style="" value="225">Vanuatu (+678)</option><option style="" value="226">Vatican City (+379)</option><option style="" value="227">Venezuela (+58)</option><option style="" value="228">Vietnam (+84)</option><option style="" value="229">Virgin Islands (+1)</option><option style="" value="230">Wallis and Futuna Islands (+681)</option><option style="" value="231">Western Sahara (+212)</option><option style="" value="232">Yemen (+967)</option><option style="" value="233">Yugoslavia (Former) (+381)</option><option style="" value="234">Zaire (+243)</option><option style="" value="235">Zambia (+260)</option><option style="" value="236">Zimbabwe (+263)</option><option style="" value="237">DR Congo (+243)</option>						</select></div>
            <div class="fleft paddl10"><input type="text" name="MOBILENO" id="MOBILENO" class="hp-regform-txtfield-new" style="width: 96px;" maxlength="20" value="Mobile Number" onfocus="if(this.value=='Mobile Number') {this.value=''; }" onblur="if(this.value=='') {this.value = 'Mobile Number'; }offTtip();"></div>
            <div class="fleft paddl5 paddt5"><img width="15" height="18" alt="Profiles in MobileShop are Mobile Verified. To ensure authenticity and credibility, we have made mobile number verification mandatory. You have the option of hiding your mobile number." title="Profiles in MobileShop are Mobile Verified. To ensure authenticity and credibility, we have made mobile number verification mandatory. You have the option of hiding your mobile number." src="https://imgs.mobileshop.com/bmimgs/hp-secure-icon-new.png" style="padding-left:2px;"></div>
          </dd>
           <div id="tooltipCN" style="position: absolute; z-index: 1000; right: 147px;  width: auto; text-align: left; font-weight:normal; display: none; width:199px; margin-top:33px;"><div style="position:absolute; left:50px; top:-10px; z-index:1001;"><div class="tiptopArrow"></div></div><div class="srhres-tooltip">Please provide your mobile number without the country code</div></div>
        </dl>	
            <input type="hidden" name="COUNTRY" id="COUNTRY" value="getcntrval" />							
        <dl>
          <dt><label for="EMAIL">Email ID</label></dt>
          <dd>
            <input type="text" name="EMAIL" id="EMAIL" maxlength="50" class="hp-regform-txtfield-new" style="width:230px;" value="">
          </dd>
        </dl> 

        <dl>
          <dt><label for="PASSWORD">Login Password</label></dt>
          <dd>
            <input type="password" autocomplete="off" name="PASSWD1" id="PASSWORD" class="hp-regform-txtfield-new" style="width:230px;" maxlength="20" value="">
          </dd>
        </dl> 
        <dl class="paddb10" style="width:385px;">

        <div class="fleft paddt5"><span class="fleft" style="margin-top:3px; display:inline-block;"><input type="checkbox" id="TERMS" name="TERMS" value="Y" checked></span><span class="fleft clr7 paddl5" style="display:inline-block; font-size:11px; line-height: 13px; width:150px;">I have read and agree to the <a href="/terms.php" target="_blank" class="link">T&amp;C</a> and <a href="/privacy-policy.php" target="_blank" class="link">Privacy Policy</a></div>




           <div class="fright" style="padding:5px 2px 0px 0px;">
              <!--<input type="hidden" name="TERMS" id="TERMS" value="Y">-->
            <input type="hidden" name="trackid" value="00500004112">
            <input type="hidden" name="formfeed" value="y">
            <input type="hidden" name="type" value="internal">
            <input type="hidden" name="hpgtrack" value="hpg">
            <input type="hidden" value="1" id="visitorrestric" name="visitorrestric">
            <input type="submit" class="hdtxt1 boldtxt clr6 paddt5 paddr15 paddb5 paddl15  txtupper" alt="Register Free" value="Register Free" style="width:155px;background:#ff7c0b;border-radius:2px;text-decoration:none;display:block;border:1px solid #ff7c0b;"/>
          </div><br clear="all">
  </dl><br>

      </div>
      <input type="hidden" value="1" id="gatrack-gender-m-count" name="gatrack-gender-m-count">
      <input type="hidden" value="0" id="gatrack-gender-f-count" name="gatrack-gender-f-count">
      <input type="hidden" name="GOSECURE" id="GOSECURE" value="Y">
      <input type="hidden" name="cookieType" value="organic">
      <input type="hidden" name="cookieVal" value="172.20.17.69;172.20.5.62::006::::0::006bingsearch::Y::2025-07-30 17:43:00::">
    </form> 
  <!-- Register Form - End --> 	
  <div class="clear"></div>
  </div>		

</div>
<iframe border=1 src='https://campaign.mobileshop.com/track/clicktrack.php?trackid=00500004112&type=internal&formfeed=y' style='display:none;'></iframe>
<!-- enquiry box right end -->				<!-- Form Ends --><div class="clear"><!--  --></div>
  </div>
</div>
</td>

  </tr>
  </table>
    <div style="padding:0px 0px 20px 220px;display:none;" id='formdiv'>
  <div id="mydiv">
    <div id="rndcorner" style="width:322px;">
        <div class="hdtittle">Member Login</div>
            <!-- Content Area -->
            <div id='log' >
              <!-- for equal div and 1024 res --> 
                                <div>
                  <div style="padding: 10px 40px;">
                    <form name="Login"  method="post" action="https://profile.mobileshop.com/login/memlogin.php?" style="margin:0px;">
                      <INPUT TYPE='HIDDEN' VALUE='LFR' NAME='dLT' id='dLT'>
                      <INPUT TYPE='HIDDEN' VALUE='https://www.mobileshop.com/login/login.php' NAME='dTHR' id='dTHR'>
                      <input type='hidden' value='' name='fpDT' id='fpDT'/>
                                            <div class="lheight120"><span id="error" class="errortxt" style="padding: 0px;display:block;line-height:14px;"></span><label for="ID"><b>Mobile Number</b> or  <b>Matrimony ID</b> or <b>E-mail</b></label><br/><input type="text" name="MID" id="MID" value="" tabindex="10" size="32" class="textfield " style="width: 225px;" onKeyUp="errorclear('MID');"></div>
                      <div class="lheight120" style="padding-top:5px;"><font class="boldtxt"><label for="PASSWORD">Password</label></font><br><input type="password" id="PASSWORD1" name="PASSWORD1" value="" tabindex="11" maxlength=20 size="32" class="textfield " style="width: 225px;" onKeyUp="errorclear('PASSWORD1');"  autocomplete="off"></div>										
                                            <div style="padding-top:5px;" class="fleft lheight120">
                        <font class="normaltxt"><input type="checkbox" class="radiomargin" value="1" name="STYLOGIN" id="STYLOGIN" checked> 
                        <label class="radiolabel" for="STYLOGIN">Keep me logged in</label></font><br>
                      </div>							
                                              <div class="fright" style="padding: 10px 17px 5px 0px;"><input class="button small" type="submit" value="Login" tabindex="12" onClick="return chkvalid();"></div><br clear="all">
                        <div style="padding-right:17px; " class="paddt3"><a href="javascript:void(0);" onclick="forgotpasswd('mlfpwd');" id="mlfpwd">Forgot Password?</a></font></div>
                    </form>
                  </div>
                </div>


              </div>
            <!-- Content Area -->
        </div>
    </div>

    <div style="width:322px;">
    <div style="padding: 8px 2px 0px 0px;text-align:right;display:block;" id="regfree" class="smalltxt">Not a member yet? <a href="https://www.mobileshop.com" tabindex="5">Click here</a> to register.	
    </div>	
  </div>
    </div>
  </div>

  <div style="display:none;" id="displaydiv1">
    <div id="rndcorner" style="float:left;width:772px;">
        <div style="padding:5px 0px 5px 11px;">
          <div style="float:left;">
              <div style="float:left;background:url(https://imgs.mobileshop.com/bmimages/tab-curve-bg.gif) repeat-x;height:41px;width:740px">

              <div style="float:left;">
                <div style="float:left;"><img src="https://imgs.mobileshop.com/bmimages/tab-lft-curve.gif" width="6" height="41"></div><div style="float:left;background:url(https://imgs.mobileshop.com/bmimages/tab-clr-right.gif) no-repeat top right;height:41px;"><div style="padding:5px 20px 0px 10px;" ><a href="" class="mediumtxt1 boldtxt clr4">Member Login</a> </div></div>
              </div>
              </div>

              <div style="float:left;background:url(https://imgs.mobileshop.com/bmimages/tr-3.gif) no-repeat;width:10px;height:41px;border:0px solid #000000;"></div>
            </div>

          <!-- Content Area -->
          <div style="width:750px;">
          <div class="bl">
            <div class="br">
              <div style="padding:10px 17px 10px 17px;">
                <div id="displaydiv3" class="smalltxt"></div>
                <div style="padding: 10px 10px 0px 0px;" id="displaydiv2" class="smalltxt"></div>

              </div>
            </div>
          </div>
          </div>
          <!-- Content Area -->
        </div>
    </div><br clear="all">
  </div></div>

    <script src="//imgs.mobileshop.com/scripts/jquery-bm-latest2020.js?v1"></script>

  <script src="//imgs.mobileshop.com/scripts/footer-accordion.js"></script>

<script> 
$(document).ready(function(){
  var gamoogaredisval = "";
  if(gamoogaredisval == 1){   
    triggergamooga(2);
  }

var spenttime = "";
var gamogatime2 = "";
var domainredis = "";

if(spenttime >= gamogatime2){
var matriid = "";
 if(parseInt(spenttime) >= parseInt(gamogatime2)){  
  triggergamooga();
    $.ajax({	
      type: "POST",												
      url: "https://profile."+domainredis+"matrimony.com/payments/gamoogaredis.php",
      dataType: "json",
      data:{'matriid':matriid,'redisset':'0'},
      success: function(res){ 
        console.log('rediscleared==>'+res); 
            //triggergamooga();				
          }					
        });
}
}


function triggergamooga(val=''){  
    console.log("gamooga yet to be triggered");	
     _ss_track.handlers.push(['connect',function() {_ss_track.api.live_chat_click(); }]);
     console.log("gamooga triggered");	
     if(val == 2){
      _ss_track.events.push(['GamoogaNonCallFlag',{"GamoogaNonCallFlag":"1"}]);
     }		 
}
});	
</script>

<div class="clear"></div>

<script>
(function() 
{
  var _fbq = window._fbq || (window._fbq = []);
  if (!_fbq.loaded) {
    var fbds = document.createElement('script');
    fbds.async = true;
    fbds.src = '//connect.facebook.net/en_US/fbds.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(fbds, s);
    _fbq.loaded = true;

  }
  _fbq.push(['addPixelId', '1427539377489703']);

})();
window._fbq = window._fbq || [];
window._fbq.push(['track', 'PixelInitialized', {}]);
</script>
<noscript><img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=1427539377489703&amp;ev=PixelInitialized" /></noscript>
<script src='https://imgs.mobileshop.com/scripts/visitor.js?random=110420221510'></script><script>if(NODECHAT!='1'){anonConnection();}</script>	<iframe src="https://profile.mobileshop.com/organic/organictrack.php?ref=https%3A%2F%2Fwww.mobileshop.com%2Flogin%2Flogin.php&userip=2409%3A4080%3A3ec0%3Aa2d4%3A3563%3A487c%3A3ef8%3Acda&page=/login/login.php&aff=&matriid=&dnam=mobileshop&ip=172.20.17.69" width=0 height=0 frameborder=0></iframe>
<link rel="stylesheet" type="text/css" href="//imgs.mobileshop.com/bmstyles/footer-accordion.css?v7">

<style>
.plusminus {
    top: 0;
}

</style>

<div style="box-sizing: content-box">		


  <style>
   .bpsidetablink {
         font-size: 12px;
         letter-spacing: .6px;
         padding: 11px 18px;
         text-align: left;
         cursor: pointer;
   }

   .bpsidetablink.bm-blk {
         padding-left: 15px;
   }

   .rghttablink1, .faq-answer  {
      font-size: 14px;
      letter-spacing: .72px;
      color: #333;
      line-height: 22px;
      text-decoration: none;
      font-family: 'Lato';
   }
   .rghttablink1, .faq-answer:hover {
      color:#000 !important;
   }

   .hptablink {
         margin-top: 5px;
   }

   @media only screen and (max-width: 767px){
      .bpsidetablink{
         padding: 6% 14%;
      }

      .bpsidetablink.bm-blk {
         padding-left: 10%;
         color: #00a03a;
      }
   }

</style>

<script src="//imgs.mobileshop.com/scripts/lodash.min.js"></script>
<script src="//imgs.mobileshop.com/scripts/Footer-Links-Populating.js?v=2"></script>
<!-- About us with Browse profile start -->
<div class="hp-abtus">

<div class="hp-wrapper"> 

<div class="mob-none">
<div class="fleft"> 
   <!-- <img src="//imgs.mobileshop.com/bmimgs/footer-bmlogo.webp" class="paddr10 lazyload" align="left" alt="MobileShop.com"/>  -->
   <div class="footer-bmlogo-image"> </div>
   <span style="font-size: 17px;letter-spacing: 1.02px;color: #000;font-weight:700;padding-top: 5px;display: inline-block;">About MobileShop</span></div>
<div class="clear"> </div>
<div class="paddt20" style="font-family: Lato;color: #666666;letter-spacing: 0.75px;font-size: 13px;text-align:left;line-height: 18px;padding-bottom:30px;border-bottom: 1px solid #ddd;">MobileShop - the pioneer in online matrimony, is the most trusted matrimony service for Millions of Indians worldwide. MobileShop has been recognised as the most trusted online matrimony service by the Brand Trust Report. We have also been featured in Limca Book of records for most number of documented marriages online. Our purpose is to build a better Mobileshop through happy marriages.</div>
<div class="txt-left paddt30" style="font-size: 17px;letter-spacing: 1.02px;color: #333333;font-weight:700;">Other Matrimony Sites</div>
</div>



<!--- Mobile Footer start -->

    <div class="footer-acc-container " >
       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head " style="padding:15px 15px 7px 15px">
        <div class="fleft"> 
              <!-- <img src="//imgs.mobileshop.com/bmimgs/footer-bmlogo.webp" class="paddr10 lazyload" align="left" style="position: relative;top: -3px;" class="lazyload"/>  -->
              <div class="footer-bmlogo-image"> </div>
              <span style="font-size: 16px;letter-spacing: 0.8px;color: #000;font-weight:700;display: inline-block;">About MobileShop</span></div>
       <span class="ftr-acc-plusminus">+</span>
       <div class="clear"></div>
        </div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad" style="font-family: Lato;color: #666666;letter-spacing: 0.75px;font-size: 13px;text-align:left;line-height: 18px;padding-bottom:30px;">
          MobileShop - the pioneer in online matrimony, is the most trusted matrimony service for Millions of Indians worldwide. MobileShop has been recognised as the most trusted online matrimony service by the Brand Trust Report. We have also been featured in Limca Book of records for most number of documented marriages online. Our purpose is to build a better Mobileshop through happy marriages.
         </div>
        </div>
       </div>

        <div class="ftr-acc-bdr">
        <div class="footer-acc-head desk-none">Other Matrimony Sites<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body disply-search" >
         <div class="ftr-cyber-pad">

<div class="accordion_container paddt10" >
      <div class="acc-width fleft" style="margin-right: 39px;">

         <div id="RegionalSitesBlock" class="acc-bdr">
            <div class="accordion_head">Regional Sites<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

         <div id="CommunityMatrimonyBlock" class="acc-bdr">
            <div class="accordion_head">Community Matrimony<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

         <div id="ReligiousSitesBlock" class="acc-bdr">
            <div class="accordion_head">Religious Sites<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

         <div id="ExclusiveSitesBlock" class="acc-bdr">
            <div class="accordion_head">Exclusive Sites<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

      </div>

      <div class="acc-width fleft">

         <div id="MandapBlock" class="acc-bdr">
            <div class="accordion_head">Mandap<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

         <div id="WeddingBazaarBlock" class="acc-bdr">
            <div class="accordion_head">WeddingBazaar<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

         <div id="CommunityShaadiBlock" class="acc-bdr">
            <div class="accordion_head">Community Shaadi<span class="plusminus">+</span></div>
            <div class="accordion_body" style="display: none;">
               <div class="cyber-pad">
                  <div class="bptab"></div>
                  <div class="bptabright"></div>
                  <div style="clear:both;"> </div>
               </div>
            </div>
         </div>

      </div>
<div class="clear"></div>
</div>
             <div class="clear"></div>
         </div>
        </div>
  </div>


      <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Help & Support<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
          <div class="ftrlink">
          <a href="/contact-us.php?gaact=HP&gasrc=FTRCONTBHARAT" target="_blank" rel="noreferrer">Contact us</a>
          <a href="/contact-us.php?viewtab=feedback&gaact=HP&gasrc=FTRFEEDBACKBHARAT" target="_blank" rel="noreferrer">Feedback</a>
          <a href="/faq.php?gaact=HP&gasrc=FTRFAQBHARAT" target="_blank" rel="noreferrer">FAQs</a>
          </div>
          <div class="clear"></div>
         </div>
        </div>
       </div>



       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Our other Services<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
            <div class="ftrlink">
                    <a href="https://www.elitematrimony.com" target="_blank" rel="noreferrer">EliteMatrimony.com</a>	
            <a href="https://play.google.com/store/apps/details?id=jodii.app" target="_blank" rel="noreferrer">Jodii</a> 
            <a target="_blank" rel="noreferrer" href="https://www.matchastro.com/">MatchAstro: Talk to astrologer</a>
            <a target="_blank" rel="noreferrer" href="https://luv.com/">Luv.com</a>
            <a target="_blank" rel="noreferrer" href="https://manyjobs.com/">ManyJobs.com</a>
                   </div>
             <div class="clear"></div>
         </div>
        </div>
       </div>
       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Social Initiatives<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
          <div class="ftrlink">
          <a title="Ability Matrimony" target="_blank" rel="noreferrer" href="http://www.abilitymatrimony.com/?Mobileshop-footer-Homepage&utm_medium=BMWeb&utm_campaign=BMfooter" rel="nofollow">AbilityMatrimony.com</a>
          </div>
          <div class="clear"></div>
         </div>
        </div>
       </div>
       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Our Wedding Services<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
          <div class="ftrlink">
          <a href="http://www.mandap.com/" target="_blank" rel="noreferrer" >Mandap.com</a>
          <a href="http://www.weddingbazaar.com/" target="_blank" rel="noreferrer">WeddingBazaar.com</a>
          <a href="//www.makemywedding.com/" target="_blank" rel="noreferrer">Make My Wedding</a>

          </div>
          <div class="clear"></div>
         </div>
        </div>
       </div>
       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Information<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
          <div class="ftrlink">
          <a href="/aboutus.php?gaact=HP&gasrc=FTRABTUSBHARAT" target="_blank" rel="noreferrer">About Us</a>
          <a href="/awards.php?gaact=HP&gasrc=FTRAWDSBHARAT" target="_blank" rel="noreferrer" >Awards</a>
          <a href="https://www.matrimony.com/milestones.php?gaact=HP&gasrc=FTRMILESBHARAT" target="_blank" rel="noreferrer" >Milestones</a>
          <a href="//profile.mobileshop.com/register/registerform.php?gaact=HP&gasrc=FTRREGBHARAT" target="_blank" rel="noreferrer" >Register Free</a>
          <a href="//profile.mobileshop.com/search/search.php?gaact=HP&gasrc=FTRSRCHBHARAT" target="_blank" rel="noreferrer" >Partner Search</a>
          <a href="//profile.mobileshop.com/login/login.php?gaact=HP&gasrc=FTRLOGINBHARAT" target="_blank" rel="noreferrer" >Member Login</a>
          <a href="/success/success.php?gaact=HP&gasrc=FTRSSBHARAT" target="_blank" rel="noreferrer">Success stories</a>
          <a href="/payments/paymentoptions.php?gaact=HP&gasrc=FTRPAYBHARAT" target="_blank" rel="noreferrer">Payment Options</a>
          <a href="http://careers.matrimony.com" target="_blank" rel="noreferrer" >Careers</a>
          <a href="//www.matrimony.com/mediaroom.php" target="_blank" rel="noreferrer">Media Room</a>
          <a href="//www.mobileshop.com/mobileshop-tv-commercials.php" target="_blank" rel="noreferrer" >TV Commercials</a>
          <a href="/advertise.php?gaact=HP&gasrc=FTRADVBHARAT" target="_blank" rel="noreferrer">Advertise with us</a>
          <a href="/terms.php?gaact=HP&gasrc=FTRTCBHARAT" target="_blank" rel="noreferrer">Terms &amp; Conditions</a>
          <a href="/privacy-policy.php?gaact=HP&gasrc=FTRPPBHARAT" target="_blank" rel="noreferrer">Privacy Policy</a>
          </div>	
          <div class="clear"></div>
         </div>
        </div>
       </div>
       <div class="ftr-acc-bdr desk-none">
        <div class="footer-acc-head">Related Matrimony Services<span class="ftr-acc-plusminus">+</span><div class="clear"></div></div>
        <div class="ftr-acc-body" style="display: none;">
         <div class="ftr-cyber-pad">
          <div class="ftrlink">
          <a target="_blank" rel="noreferrer" href="http://www.happymarriages.com" >HappyMarriages.com</a>
          <a href="//www.mobileshop.com/safe-matrimony/" target="_blank" rel="noreferrer" >Safe Matrimony</a>
          <a href="/matrimony-tools.php?gaact=HP&gasrc=FTRMATTOOLSBHARAT" target="_blank" rel="noreferrer">Matrimonial Tools</a>
          <a href="//www.mobileshop.com/matrimonial-listings?gaact=HP&gasrc=FTRMATSITESBHARAT" target="_blank" rel="noreferrer">Matrimonial Sites</a>
          <a target="_blank" rel="noreferrer" href="//profile.mobileshop.com/matrimonial?gaact=HP&gasrc=FTRMONIALSBHARAT" >Mobile Shops</a>
          <a target="_blank" rel="noreferrer" href="//www.mobileshop.com/search/community-matrimony-sites.php?gaact=HP&gasrc=FTRMATWEBSITESBHARAT" >Matrimonial Websites</a>
          <a href="/matrimonyoutlets.php?gaact=HP&gasrc=FTRBRANCHESBHARAT" >Mobile Shop Retail Stores</a>
          <a target="_blank" rel="noreferrer" href="http://www.mandap.com/" >Marriage Halls</a>
          <a target="_blank" rel="noreferrer" href="http://www.mandap.com/">Banquet Halls </a>


          </div>
          <div class="clear"></div>
         </div>
        </div>
       </div>


    </div>

  <!--- Mobile Footer End -->

</div>

</div>
 <div class="clear"></div>
<!-- About us with Browse profile End -->
<style>
.ftrcol-1 {height: 503px;}
</style>	
<!-- Footer new Start  -->
<div class="hp-wrapper ftr-mrg mob-none"> 
   <div class="ftrcol-1 fleft"> 
   <div class="ftr-hd paddt15">Regional Matrimony <br/>Services </div>
   <div class="ftrlink paddt15">
       <a href="//www.assamesematrimony.com" target="_blank" rel="noreferrer" title="Assamese Matrimony">Assamese Matrimony</a>
       <a href="//www.bengalimatrimony.com" target="_blank" rel="noreferrer" title="Bengali Matrimony">Bengali Matrimony</a>
       <a href="//www.biharimatrimony.com" target="_blank" rel="noreferrer" title="Bihari Matrimony">Bihari Matrimony</a>	
       <a href="//www.gujaratimatrimony.com" target="_blank" rel="noreferrer" title="Gujarati Matrimony">Gujarati Matrimony</a>
       <a href="//www.hindimatrimony.com" target="_blank" rel="noreferrer" title="Hindi Matrimony">Hindi Matrimony</a>
       <a href="//www.kannadamatrimony.com" target="_blank" rel="noreferrer" title="Kannada Matrimony">Kannada Matrimony</a>
       <a href="//www.keralamatrimony.com" target="_blank" rel="noreferrer" title="Kerala Matrimony">Kerala Matrimony</a>
       <a href="//www.marathidating.com" target="_blank" rel="noreferrer" title="Marathi Dating">Marathi Dating</a>
       <a href="//www.marwadimatrimony.com" target="_blank" rel="noreferrer" title="Marwadi Matrimony">Marwadi Matrimony</a>
       <a href="//www.oriyamatrimony.com" target="_blank" rel="noreferrer" title="Oriya Matrimony">Oriya Matrimony</a>
       <a href="//www.parsimatrimony.com" target="_blank" rel="noreferrer" title="Parsi Matrimony">Parsi Matrimony</a>
       <a href="//www.punjabimatrimony.com" target="_blank" rel="noreferrer" title="Punjabi Matrimony">Punjabi Matrimony</a>
       <a href="//www.rajasthanimatrimony.com" target="_blank" rel="noreferrer" title="Rajasthani Matrimony">Rajasthani Matrimony</a>	
       <a href="//www.sindhimatrimony.com" target="_blank" rel="noreferrer" title="Sindhi Matrimony">Sindhi Matrimony</a>	
       <a href="//www.tamilmatrimony.com" target="_blank" rel="noreferrer" title="Tamil Matrimony">Tamil Matrimony</a>
       <a href="//www.telugumatrimony.com" target="_blank" rel="noreferrer" title="Telugu Matrimony">Telugu Matrimony</a>
       <a href="//www.urdumatrimony.com" target="_blank" rel="noreferrer" title="Urdu Matrimony">Urdu Matrimony</a>	
   </div>
   <div class="clear"></div>
 </div>
 <div class="ftrcol-2 fleft"> 
 <div class="ftr-hd paddt15">Help & Support</div>
 <div class="ftrlink paddt15">
    <a href="/contact-us.php?gaact=HP&gasrc=FTRCONTBHARAT" target="_blank" rel="noreferrer">Contact us</a>
    <a href="/contact-us.php?viewtab=feedback&gaact=HP&gasrc=FTRFEEDBACKBHARAT" target="_blank" rel="noreferrer">Feedback</a>
    <a href="/faq.php?gaact=HP&gasrc=FTRFAQBHARAT" target="_blank" rel="noreferrer">FAQs</a>
 </div>	
 <div class="clear"></div>

 <div class="ftr-hd paddt15">Our other Services</div>
 <div class="ftrlink paddt15">
     <a href="https://www.elitematrimony.com" target="_blank" rel="noreferrer">EliteMatrimony.com</a>
  <a href="https://play.google.com/store/apps/details?id=jodii.app" target="_blank" rel="noreferrer">Jodii</a> 
  <a target="_blank" rel="noreferrer" href="https://www.matchastro.com/">MatchAstro: Talk to astrologer</a>
  <a target="_blank" rel="noreferrer" href="https://luv.com/">Luv.com</a>
  <a target="_blank" rel="noreferrer" href="https://manyjobs.com/">ManyJobs.com</a>
 </div>
 <div class="clear"></div>

 <div class="ftr-hd paddt15">Our Wedding Services</div>
 <div class="ftrlink paddt15">
    <a href="//www.mandap.com/" target="_blank" rel="noreferrer" >Mandap.com</a>
    <a href="//www.weddingbazaar.com/" target="_blank" rel="noreferrer">WeddingBazaar.com</a>
  <a href="//www.makemywedding.com/" target="_blank" rel="noreferrer">Make My Wedding</a>

 </div>
 <div class="clear"></div>


 </div>

 <div class="ftrcol-3 fleft"> 
    <div class="ftr-hd paddt15">Information</div>
    <div class="ftrlink paddt15">
          <a href="/aboutus.php?gaact=HP&gasrc=FTRABTUSBHARAT" target="_blank" rel="noreferrer">About Us</a>
          <a href="/awards.php?gaact=HP&gasrc=FTRAWDSBHARAT" target="_blank" rel="noreferrer" >Awards</a>
          <a href="https://www.matrimony.com/milestones.php?gaact=HP&gasrc=FTRMILESBHARAT" target="_blank" rel="noreferrer" >Milestones</a>
          <a href="//www.mobileshop.com/register/registerform.php?gaact=HP&gasrc=FTRREGBHARAT" target="_blank" rel="noreferrer" >Register Free</a>
          <a href="//profile.mobileshop.com/search/search.php?gaact=HP&gasrc=FTRSRCHBHARAT" target="_blank" rel="noreferrer" >Partner Search</a>
          <a href="//www.mobileshop.com/login/login.php?gaact=HP&gasrc=FTRLOGINBHARAT" target="_blank" rel="noreferrer" >Member Login</a>
          <a href="/success/success.php?gaact=HP&gasrc=FTRSSBHARAT" target="_blank" rel="noreferrer">Success stories</a>
          <a href="/payments/paymentoptions.php?gaact=HP&gasrc=FTRPAYBHARAT" target="_blank" rel="noreferrer">Payment Options</a>
          <a href="http://careers.matrimony.com" target="_blank" rel="noreferrer" >Careers</a>
          <a href="//www.matrimony.com/mediaroom.php" target="_blank" rel="noreferrer">Media Room</a>
          <a href="//www.mobileshop.com/mobileshop-tv-commercials.php" target="_blank" rel="noreferrer" >TV Commercials</a>
          <a href="/advertise.php?gaact=HP&gasrc=FTRADVBHARAT" target="_blank" rel="noreferrer">Advertise with us</a>
          <a href="/terms.php?gaact=HP&gasrc=FTRTCBHARAT" target="_blank" rel="noreferrer">Terms &amp; Conditions</a>
          <a href="/privacy-policy.php?gaact=HP&gasrc=FTRPPBHARAT" target="_blank" rel="noreferrer">Privacy Policy</a>
    </div>	
    <div class="clear"></div>
 </div>

 <div class="ftrcol-4 fleft"> 
   <div class="ftr-hd paddt15">Related Matrimony <br/> Services</div>
   <div class="ftrlink paddt15">
   <a target="_blank" rel="noreferrer" href="http://www.happymarriages.com" >HappyMarriages.com</a>
  <a href="//www.mobileshop.com/matrimonial-listings?gaact=HP&gasrc=FTRMATSITESBHARAT" target="_blank" rel="noreferrer">Matrimonial Sites</a>
 <a target="_blank" rel="noreferrer" href="//www.mobileshop.com/search/community-matrimony-sites.php?gaact=HP&gasrc=FTRMATWEBSITESBHARAT" >Matrimonial Websites</a>
 <a href="/matrimonyoutlets.php?gaact=HP&gasrc=FTRBRANCHESBHARAT" >Mobile Shop Retail Stores</a>
   </div>
 </div>
 <div class="clear"></div>	
</div> 	
<div class="clear"></div>




 <div class="hp-wrapper ftrcpy">

 <div class="fleft ftrbtm1" >
 <div  class="">This website is strictly for matrimonial purpose only and not a dating website.</div>
 <div class="">Copyright  &copy; 2025. All rights reserved.</div>
 </div>


 <div class="fleft ftrbtm2">
 <div class="fleft"><img height="60" width="59" src="//imgs.mobileshop.com/bmimgs/limca-book.webp" alt="Limca book" class="lazyload"></div>
 <div class="fleft paddl10">The Limca Book <br>of records <br>Highest Number of Marriages</div>
 </div>


 <div class="fleft ftrbtm4" >
 <div style="#color: #4a546e;font-size: 15px;">Follow Us on:</div>
 <ul class="ftrsocial-list">
 <li><a target="_blank" rel="noreferrer" href="https://www.facebook.com/MobileShop"><img  height="20" width="20" src="//imgs.mobileshop.com/bmimgs/fb-icon.webp" alt="Facebook" class="lazyload"></a></li>
 <li><a target="_blank" rel="noreferrer" href="https://www.twitter.com/mobileshop"><img  height="18" width="20" src="//imgs.mobileshop.com/bmimgs/twitter-icon.webp" alt="Twitter" class="lazyload"></a></li>
 <li><a target="_blank" rel="noreferrer" href="https://www.instagram.com/mobileshop"><img  height="20" width="20" src="//imgs.mobileshop.com/bmimgs/instagrram-icon.webp" alt="Instagram" class="lazyload"></a></li>
 </ul>
 </div>

<div class="clear"></div>
 </div>
<!-- Footer new End  -->

</div>


 <script src="//imgs.mobileshop.com/scripts/footer-accordion.js?v7"></script>	
</center>

        <script language="javascript" type="text/javascript">
      $(document).ready(function(){
        $(".litebox").colorbox($.extend({scrolling:false}, getParameters()));
      });	
      </script>




  <script type="text/javascript">
    var _ss_track = {};

    /* your customization options */
    _ss_track.options = {};

    /* Donot edit below this line */
          _ss_track.id = "206f307a-c1bf-41ec-8ac6-8d0b3a07ace5";
        _ss_track.events = []; _ss_track.handlers = []; _ss_track.alarms = [];
    (function() {
      var ss = document.createElement('script'); ss.type = 'text/javascript'; ss.async = true; ss.id = "__ss";
      //ss.src = '//d1011upzeqfr3c.cloudfront.net/static/ssclient.min.js';

            ss.src = '//cdn-jp.gsecondscreen.com/static/ssclient.min.js';
            var fs = document.getElementsByTagName('script')[0]; fs.parentNode.insertBefore(ss, fs);
    })();
  </script>





<!-- Google Analytics Scripts starts -->
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', "UA-BSF6LN3TTX-1"]);
  _gaq.push(['_setDomainName', "mobileshop.com"]);
    _gaq.push(["_setCustomVar", 1, "User", "V", 2]); 
    _gaq.push(['_setAllowLinker', true]);
      _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

  function APPdownloadGA(GASRC,GAACT,category){
  ga('send', {'hitType': 'event', 'eventCategory': category, 'eventAction': GASRC, 'eventLabel': GAACT});
}	
</script>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-BSF6LN3TTX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-BSF6LN3TTX');
    function ga(se,ev,category,gamodule,action,nan){
      if(se=='send'){ 
        gtag('event',category,{'event_category':action,'event_label':gamodule});
      }
    }
    function gaq(){ 
      this.push = function(ev){
        if(ev[0]=='_trackEvent'){
          gtag('event',ev[1],{'event_category':ev[2],'event_label':ev[3]});	
        }	
      }
    }
    var _gaq = new gaq();
  </script>
<!-- Google Analytics Scripts ends -->

<script type="text/javascript" language="javascript">
      function closeChromeBar(){
        //setCookie('CHROMEBANNERCLOSE','1');
        $('#chromeinfobar').slideUp('slow', function(){
          $('#topnavlog').removeClass('topnavlog');					
          $('#fixed-topnav').removeClass('topnav');
          $('#fixed-topnavbar').removeClass('topnavbar');
          $('#topnavwrapper').removeClass('chrommrgt30');					
        });
      }
      $(window).load(function(){
      var bminstall = document.getElementById("bmchmextverifyinstall");
      if(bminstall==null && window.chrome){
        $('#topnavlog').addClass('topnavlog');
        $('#fixed-topnav').addClass('topnav');
        $('#fixed-topnavbar').addClass('topnavbar');
        $('#topnavwrapper').addClass('chrommrgt30');
        $('#chromeinfobar').slideDown('slow');
        //setCookieWithExpiry('CHROMEBANNERCLOSE','4',14);
      }
    });
    function chmGATrack(chmVersion,content){
        var path = '/GAVirtual/ChromeV'+chmVersion.toString()+'/'+content;
        var pushval = _gaq.push(['_trackPageview',path]);				
    }
</script>



<!-- Begin Consolidated GA Tracking -->
  <script type="text/javascript">
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-33448923-13', "mobileshop.com"); 
    ga('send', 'pageview');
    ga('set', 'dimension1', "V");


  </script>
<!-- End Consolidated GA Tracking -->




<!-- Conversion Pixel - YOptima_MobileShop_LP_8771178 - DO NOT MODIFY -->
<script src="https://secure.adnxs.com/px?id=859538&seg=8771178&t=1" type="text/javascript"></script>
<!-- End of Conversion Pixel -->

<!-- Facebook Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '144259622883989');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=144259622883989&ev=PageView&noscript=1"/></noscript>
<!-- End Facebook Pixel Code -->

<!-- Bing Pixel Code -->
<script>(function(w,d,t,r,u){var f,n,i;w[u]=w[u]||[],f=function(){var o={ti:"5104938"};o.q=w[u],w[u]=new UET(o),w[u].push("pageLoad")},n=d.createElement(t),n.src=r,n.async=1,n.onload=n.onreadystatechange=function(){var s=this.readyState;s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)},i=d.getElementsByTagName(t)[0],i.parentNode.insertBefore(n,i)})(window,document,"script","//bat.bing.com/bat.js","uetq");</script><noscript><img src="//bat.bing.com/action/0?ti=5104938&Ver=2" height="0" width="0" style="display:none; visibility: hidden;" /></noscript>
<!-- Bing Pixel Code -->

<!-- Twitter universal website tag code -->
<script>
!function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
},s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='//static.ads-twitter.com/uwt.js',
a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
twq('init','nvlsm');
twq('track','PageView');
</script>
<!-- End Twitter universal website tag code -->



<script type="text/javascript">
var bdpallow = '0';

if(bdpallow == 1){
  $(document).ready(function(){
    if(jStorage.get("basicdetpop_")){

      var logTimeBD = jStorage.get("logindiffbasicdet_");
      var currTimeBD = '1753877580';
      var diffTimeBD = parseInt(currTimeBD) - logTimeBD;

      if(diffTimeBD >= 14400){
        var getBasicDetCount = jStorage.get("basicdetpop_");
        var totBasicDetCount = getBasicDetCount+1;		
        var remBasicDetTime = jStorage.getTTL("basicdetpop_");		
        var remDiffBasicDetTime = jStorage.getTTL("logindiffbasicdet_");		
        jStorage.set("basicdetpop_", totBasicDetCount, {TTL: remBasicDetTime});				
        jStorage.set("logindiffbasicdet_", parseInt(currTimeBD), {TTL: remDiffBasicDetTime});
      }
    }else{
      jStorage.set("basicdetpop_", 1, {TTL: 2592000000});
      var currentBasicDetTime = '1753877580';			
      jStorage.set("logindiffbasicdet_", parseInt(currentBasicDetTime), {TTL: 2592000000});			
    }

    var dispPopup = jStorage.get("basicdetpop_");

    if(dispPopup == 3){
      window.setTimeout(function() {
        urlBasicDet = "https://profile.mobileshop.com/template/basicdetpopup.php";					
        $("#cboxOverlay").css("background", "#000");					
        $.colorbox({open:true, opacity:0.60,open:true,href:urlBasicDet,width:600,height:380});					
        $("#cboxTopCenter,#cboxTopLeft,#cboxBottomCenter,#cboxBottomRight,#cboxBottomLeft,#cboxTopRight,#cboxTopCenter,#cboxTopLeft,#cboxMiddleLeft,#cboxMiddleRight,#cboxClose").hide();
      }, 5000);
    }
  });
}
</script>
<script language="javascript">
//Registraion page drop out log tracking
function regPDLogTrackAjax(targetUrl)
{     
   if(typeof(targetUrl) === 'object')
   {
    var encodedTargetUrl = btoa(targetUrl.getAttribute("href"));
   }
   else
   {
    var encodedTargetUrl = btoa(targetUrl);
   }
     var encodedCurrentUrl = btoa(window.location.href);   
    $.ajax({
        type: "POST",
        url: "//www.mobileshop.com/register/ajaxRegCurlTrack.php",
        data: "regCurrentUrl="+encodedCurrentUrl+"&regTargetUrl="+encodedTargetUrl+"&pageName=PAGE1&regTrckDomainName=mobileshop",
        crossDomain:true,
        success: function(msg){
             if(msg != ""){
             }
        }
    });
}
</script>




</body>
</html>
  <script type="text/javascript">
  var mobFlagScript = "0";
    function otplogin(e) {
    loginHideShow("resLoginForm","resLoginViaOtp");
    $("#loginviaotp").css("display","block");
    resetInputValues();
  }

  //By default clear the values
  function resetDom(){
    $("#loginviaotp").css("display","none");
    $("#otppageid").css("display","none");	
    $("#forgotpassword").css("display","none");
    $("#forgetOtpPageid").css("display","none");
    $("#newpassword").css("display","none");
    $("#multiids").css("display","none");

    $("#errorpop").css("display","none");
    $("#errorpop1").css("display","none");
    $("#errorpop2").css("display","none");	
    $("#forgeterrorpop1").css("display","none");
    $("#forgeterrorpop2").css("display","none");	
    $("#errorpop3").css("display","none");
    $("#errorpop4").css("display","none");	
    $("#errorPopOtpID").css("display","none");
    $("#forgetErrorPop").css("display","none");
  }

  function resetInputValues(){
    $("#MIDP").val("");
    $("#PASSWORD2").val("");
    $("#otploginID").val("");
    $("#otppin").val("");
    $("#forgotpwdid").val("");
    $("#forgetotppin").val("");
    $("#newpass").val("");
    $("#confpass").val("");
  }

  function loginHideShow(hideDiv,showDiv) {
    resetDom();	
    $("#"+hideDiv).css("display","none");
    $("#"+showDiv).css("display","block");
      }

  function forgotpasswd(e) {		
    loginHideShow("resLoginForm","resLoginViaOtp");
    $("#forgotpassword").css("display","block");
    resetInputValues();
  }
    var mobFlagScript = "0";
  var domainshortnameFlag = "1";
  var MatriIderr = "Login with Matrimony Id is not valid now. Retry with Mobile No. / E-Mail ID";
  var Matriidnotvalild = "You cannot use Matri Id. Reset password with Mobile No. / E-Mail ID"; 
  var EnterMoborEmailErr = "Enter Mobile No. / E-Mail ID."; 
  var EnterValidMoborEmailErr = "Enter Valid Mobile No. / E-Mail ID"; 
  //Login via otp
  function chkValidOtpID()
  {
    var id = $('#otploginID').val(); 
    ga('send','event','LoginViaOTP-WEB-Mobileshop','Mobile No-Email-Matri','Submit');
    ga('tracker1.send','event','LoginViaOTP-WEB-Mobileshop','Mobile No-Email-Matri','Submit',{'nonInteraction': true});
    if(id == "")
    {
      $("#errorPopOtpID").css("display","block");
      if( domainshortnameFlag == 1){
        $("#errorPopOtpID").html(EnterMoborEmailErr);
      }
      else{
        $("#errorPopOtpID").html("Enter Mobile Number / Matri ID / E-Mail ID.");
      }
      $("#otploginID").focus();
      return false;
    }
    else if((validatePhoneNumber(id) || validateEmail(id)) && id != '')
    {	
      //$("#loginviaotp").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#loading").css("display","block");
      $("#loadpopup").html('<center><img src="https://imgs.mobileshop.com/bmimgs/small_loading.gif"></center>')
      $("#loadpopup").css("margin-top","60px");
      $('#otppin').val(''); 
      var params = 'ID='+ id+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1";
      $.ajax({
        type: "POST",
        url: "https://api.mobileshop.com/applogin/otp-login.php",
        dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {
          data = ConvertKeysToUpperCase(data);					
          var result = jQuery.parseJSON(JSON.stringify(data));									
          $("#otpMobNum").html(result.MOBILENO);
          if(result.RESPONSECODE == 1 && result.ERRCODE == 0 && result.INACTIVE == 1)
          {			    	
            $("#loading").css("display","none");
            $("#errorPopOtpID").css("display","block");
            $("#loginviaotp").css("display","block");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            $("#errorPopOtpID").html("Sorry! Incorrect login details.");
            $("#otploginID").focus();
          }
          else if((result.RESPONSECODE == 1 && result.ERRCODE == 0) || (result.RESPONSECODE == 2 && result.ERRCODE == 72))
          {		
            $("#loading").css("display","none");
            $("#errorPopOtpID").css("display","none");
            $("#loginviaotp").css("display","none");
            $("#otppageid").css("display","block");
            $("#otppageids").css("display","none");			    				
            if(result.MOBILENO!=''){
              $("#mobileno").html(result.MOBILENO);
            }
            $('#loginid').val(id);
          }	
          else if(result.RESPONSECODE == 2 && result.ERRCODE == 1)
          {
            $("#loading").css("display","none");
            $("#errorPopOtpID").css("display","block");
            $("#loginviaotp").css("display","block");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            $("#errorPopOtpID").html(result.MESSAGE);
            $("#otploginID").focus();
          }	
          else if(result.RESPONSECODE == 2 && result.ERRCODE == 43)
          {						
            $("#loading").css("display","none");
            $("#errorPopOtpID").css("display","block");
            $("#loginviaotp").css("display","block");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            if(domainshortnameFlag == 1){
              $("#errorPopOtpID").html(EnterValidMoborEmailErr);
            }else{
              $("#errorPopOtpID").html(result.MESSAGE);
            }
            $("#otploginID").focus();
          }
          else{						
            loginHideShow('loginviaotp','otppageid');
            return false;
          }		    	

        }
      });			
    }else if(validateMatriId(id)){

        if( domainshortnameFlag == 1){
        $("#errorPopOtpID").css("display","block");
          $("#errorPopOtpID").html(MatriIderr);
          return false;
        }else{
          $("#otppageid").css("display","none");
          $("#otppageids").css("display","none");
          $("#loading").css("display","block");
          $("#loadpopup").html('<center><img src="https://imgs.mobileshop.com/bmimgs/small_loading.gif"></center>')
          $("#loadpopup").css("margin-top","60px");
          $('#otppin').val(''); 
          var params = 'ID='+ id+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1";
          $.ajax({
            type: "POST",
            url: "https://api.mobileshop.com/applogin/otp-login.php", //Directly calls apps server
            dataType: "jsonp",
            crossOrigin: true,
            data: params,
            success: function(data) {
              data = ConvertKeysToUpperCase(data);					
              var result = jQuery.parseJSON(JSON.stringify(data));									
              $("#otpMobNum").html(result.MOBILENO);
              //alert(result.RESPONSECODE);
              console.log(result);
              if(result.RESPONSECODE == 1 && result.ERRCODE == 0 && result.INACTIVE == 1)
              {			    	
                $("#loading").css("display","none");
                $("#errorPopOtpID").css("display","block");
                $("#loginviaotp").css("display","block");
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","none");
                $("#errorPopOtpID").html("Sorry! Incorrect login details.");
                $("#otploginID").focus();
              }
              else if((result.RESPONSECODE == 1 && result.ERRCODE == 0) || (result.RESPONSECODE == 2 && result.ERRCODE == 72))
              {
                  $("#loading").css("display","none");
                  $("#errorPopOtpID").css("display","none");
                  $("#loginviaotp").css("display","none");
                  $("#otppageid").css("display","block");
                  $("#otppageids").css("display","none");			    				
                  if(result.MOBILENO!=''){
                    $("#mobileno").html(result.MOBILENO);
                  }
                  $('#loginid').val(id);
              }	
              else if(result.RESPONSECODE == 2 && result.ERRCODE == 1)
              { 
                $("#loading").css("display","none");
                $("#errorPopOtpID").css("display","block");
                $("#loginviaotp").css("display","block");
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","none");
                $("#errorPopOtpID").html(result.MESSAGE);
                $("#otploginID").focus();
              }	
              else if(result.RESPONSECODE == 2 && result.ERRCODE == 43)
              {	$("#loading").css("display","none");
                $("#errorPopOtpID").css("display","block");
                $("#loginviaotp").css("display","block");
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","none");
                if(domainshortnameFlag == 1){
                  $("#errorPopOtpID").html(EnterMoborEmailErr);
                }else{
                  $("#errorPopOtpID").html(result.MESSAGE);
                }
                $("#otploginID").focus();
              }
              else{					
                loginHideShow('loginviaotp','otppageid');
                return false;
              }		    	

            }
          });
        }

    }
    else if(!(validatePhoneNumber(id)) || !(validateEmail(id)) || !(validateMatriId(id)))		
    {
      $("#errorPopOtpID").css("display","block");
      if(domainshortnameFlag == 1){
          $("#errorPopOtpID").html(EnterValidMoborEmailErr);
        }else{
          $("#errorPopOtpID").html("Enter Valid Mobile Number / Matri ID / E-Mail ID.");
        }
      return false;
    } 

  }
  //Forgot password
  function checkvalid()
  {	
    var id = $('#forgotpwdid').val(); 
    if(id == "")
    {			
      $("#forgotpassword").css("display","block");			
      $("#forgetErrorPop").css("display","block");
      if(domainshortnameFlag == 1){
        $("#forgetErrorPop").html(EnterMoborEmailErr);
      }
      else{
        $("#forgetErrorPop").html("Enter Mobile Number / Matri ID / E-Mail ID.");
      }
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","none");
      $("#successpage").css("display","none");		    
      $("#forgotpwdid").focus();
    }		
    else if((validatePhoneNumber(id) || validateEmail(id)) && id != '')
    {	
      $("#loading").css("display","block");
      $("#loadpopup").html('<center><img src="https://imgs.mobileshop.com/bmimgs/small_loading.gif"></center>')
      $("#loadpopup").css("margin-top","60px");
      $('#forgetotppin').val("")
      var params = 'ID='+ id+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1&RESETTYPE=1&PAGETYPE=1";
      $.ajax({
        type: "POST",
        url: "https://api.mobileshop.com/applogin/appforgotpassword.php",
        dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {
          data = ConvertKeysToUpperCase(data);				
          var result = jQuery.parseJSON(JSON.stringify(data));					
          if((result.RESPONSECODE == 2 && result.ERRCODE == 2) || (result.RESPONSECODE == 2 && result.ERRCODE == 44))
          {			    	
            $("#forgetErrorPop").css("display","none");
            $("#loading").css("display","none");
            $("#forgotpassword").css("display","block");
            $("#forgetErrorPop").css("display","block");
            $("#forgetErrorPop").html("Sorry! Incorrect login details.");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");
            $("#successpage").css("display","none");
            $("#forgotpwdid").focus();
          }
          else if(result.RESPONSECODE == 1 && result.ERRCODE == 0)
          {		
            $("#loading").css("display","none");
            $("#forgetErrorPop").css("display","none");
            $("#forgotpassword").css("display","none");
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");
            $("#successpage").css("display","none");
            $("#fpwdid").val(id);
            $("#forgotpwdid").focus();
            loginHideShow('forgotpassword','forgetOtpPageid');					
          }	
          else if(result.RESPONSECODE == 2 && result.ERRCODE == 120)
          {
            $("#loading").css("display","none");
            $("#forgetErrorPop").css("display","block");
            $("#forgotpassword").css("display","block");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");
            $("#successpage").css("display","none");
            $("#forgetErrorPop").html("You have exceeded the maximum attempts to send the OTP.");
            $("#forgotpwdid").focus();
          }

        }
      });			
    }
    else if(validateMatriId(id)){
      if( domainshortnameFlag == 1){
        $("#forgotpassword").css("display","block");
        $("#forgetErrorPop").css("display","block");
        $("#forgetErrorPop").html(Matriidnotvalild);
        $("#otppageid").css("display","none");
        $("#otppageids").css("display","none");
        $("#newpassword").css("display","none");
        $("#successpage").css("display","none");		    
        $("#forgotpwdid").focus();	
      }
      else{
        $("#loading").css("display","block");
        $("#loadpopup").html('<center><img src="https://imgs.mobileshop.com/bmimgs/small_loading.gif"></center>')
        $("#loadpopup").css("margin-top","60px");
        $('#forgetotppin').val("")
        var params = 'ID='+ id+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1&RESETTYPE=1&PAGETYPE=1";
        $.ajax({
          type: "POST",
          url: "https://api.mobileshop.com/applogin/appforgotpassword.php",
          dataType: "jsonp",
          crossOrigin: true,
          data: params,
          success: function(data) {
            data = ConvertKeysToUpperCase(data);				
            var result = jQuery.parseJSON(JSON.stringify(data));					
            if((result.RESPONSECODE == 2 && result.ERRCODE == 2) || (result.RESPONSECODE == 2 && result.ERRCODE == 44))
            {			    	
              $("#forgetErrorPop").css("display","none");
              $("#loading").css("display","none");
              $("#forgotpassword").css("display","block");
              $("#forgetErrorPop").css("display","block");
              $("#forgetErrorPop").html("Sorry! Incorrect login details.");
              $("#otppageid").css("display","none");
              $("#otppageids").css("display","none");
              $("#newpassword").css("display","none");
              $("#successpage").css("display","none");
              $("#forgotpwdid").focus();
            }
            else if(result.RESPONSECODE == 1 && result.ERRCODE == 0)
            {		
              $("#loading").css("display","none");
              $("#forgetErrorPop").css("display","none");
              $("#forgotpassword").css("display","none");
              $("#otppageids").css("display","none");
              $("#newpassword").css("display","none");
              $("#successpage").css("display","none");
              $("#fpwdid").val(id);
              $("#forgotpwdid").focus();
              loginHideShow('forgotpassword','forgetOtpPageid');					
            }	
            else if(result.RESPONSECODE == 2 && result.ERRCODE == 120)
            {
              $("#loading").css("display","none");
              $("#forgetErrorPop").css("display","block");
              $("#forgotpassword").css("display","block");
              $("#otppageid").css("display","none");
              $("#otppageids").css("display","none");
              $("#newpassword").css("display","none");
              $("#successpage").css("display","none");
              $("#forgetErrorPop").html("You have exceeded the maximum attempts to send the OTP.");
              $("#forgotpwdid").focus();
            }

          }
        });	
      }
    }
    else if(!(validatePhoneNumber(id)) || !(validateEmail(id)) || !(validateMatriId(id)))		
    {
      $("#forgotpassword").css("display","block");
      $("#forgetErrorPop").css("display","block");
      if(domainshortnameFlag == 1){
        $("#forgetErrorPop").html(EnterValidMoborEmailErr);	
      }
      else{
        $("#forgetErrorPop").html("Enter Valid Mobile Number / Matri ID / E-Mail ID.");
      }				
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","none");
      $("#successpage").css("display","none");		    
      $("#forgotpwdid").focus();
    } 				
  }

  function validatePhoneNumber(id)
  {
    var mobileregex = /^(\+91-|\+91|0)?\d{7,12}$/;
    return mobileregex.test(id);
  }   

  function validateEmail(id) 
  {
    var emailregex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return emailregex.test(id);
  }      

  function validateMatriId(id)
  {
    var matriidregex = /^[a-zA-Z][0-9]{5,8}$/;
    return matriidregex.test(id);
  } 

  function ConvertKeysToUpperCase(obj) {
    var json = JSON.stringify(obj);
    var newJson = json.replace(/"([\w]+)":/g, function($0, $1) {
    return ('"' + $1.toUpperCase() + '":');
    });
    var newObj = JSON.parse(newJson);
    return newObj;
  }

  function chkotpvalid()
  {
    var userotp = $('#otppin').val(); 
    var matriId = $('#otploginID').val(); 	
    ga('send', 'event','LoginViaOTP-WEB-Mobileshop','OTP-PIN','Submit'); 
    ga('tracker1.send','event','LoginViaOTP-WEB-Mobileshop','OTP-PIN','Submit',{'nonInteraction': true});		

    if(userotp=='')
    {
      $("#errorpop1").css("display","block");
      $("#errorpop1").html("Please Enter the OTP.");
      $("#otppin").focus();
      return false;	
    }
    else
    {
      params="ID="+matriId+"&LOGINOTP="+userotp+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1";
      $.ajax({
          type: "POST",
          url: "https://api.mobileshop.com/applogin/otp-login-validation.php",
          dataType: "jsonp",
          crossOrigin: true,
          data: params,
          success: function(data) {	
            data = ConvertKeysToUpperCase(data);
            var result = jQuery.parseJSON(JSON.stringify(data));
            if(result.RESPONSECODE == 2 && result.ERRCODE == 2)
            {			    		
              $("#errorpop1").css("display","block");
              //$("#errorpop1").html("You have entered incorrect OTP.");
              $("#errorpop1").html(result.ERRMSG);
              $("#otppin").focus();
              return false;	
            }
            else if(result.RESPONSECODE == 1 && result.ERRCODE == 0)
            {
              if(result.TOTALIDS > 1)
              {
                var profdet = JSON.stringify(result.PROFILEIDS.PROFILEID);
                var finalresult = '<form name="matriidtootpfrm"><div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick=loginHideShow("multiids","otppageid")> Choose Matri ID</div><div class="col-md-12 col-12 xs-form-pad"><div class="col-md-12 col-12 xs-banner-margin md-none"><img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1"></div><div class="login-label">';
                  for (var i=0; i < result.TOTALIDS ; i++) 
                  { 
                    let domain = result.PROFILEIDS.PROFILEID[i].DOMAIN;
                    let capitalized_domain = domain.replace(/^./, domain[0].toUpperCase()); //converting first letter to uppercase
                    finalresult+='<div class="col-md-12 col-12 float-left pt-0 xs-text-left text-left login-normal-txt"><div class="input-radio-login"><label><input type="radio" class="mr-1" name="matriid" value="'+result.MATRIID[i]+'" checked>'+result.PROFILEIDS.PROFILEID[i].MATRIID+'</label><span id="domain" class="ml-2">'+capitalized_domain+'Matrimony</span></div></div>'
                  }
          finalresult+='<div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-one"><input type="button" value="CONTINUE" class="login-btn" name="otpuserLogin"  onClick=checkedid("'+userotp+'","'+matriId+'")></div><div class="clear"></div></div></div></form>';
                $("#loading").css("display","none");
                $("#errorpop").css("display","none");			    			
                $("#loginviaotp").css("display","none");
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","block");
                loginHideShow('forgetOtpPageid','multiids');
                $("#multiids").html(finalresult);
              }
              else
              {
                location.href = result.REDIRECTURL;
              }
            }			    	
          }
        });
      }
  }	

  function forgetpwdchkotpvalid()
  {

    var userotp = $('#forgetotppin').val(); 
    var userid = $('#fpwdid').val();	
    if(userotp=='')
    {			
      $("#forgeterrorpop1").css("display","block");
      $("#forgeterrorpop1").html("Please Enter the OTP.");
      $("#forgotpassword").css("display","none");
      $("#errorpop").css("display","block");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","none");
      $("#successpage").css("display","none");
      $("#forgetotppin").focus();
      return false;	
    }
    else
    {
      params="PINNO="+userotp+"&ID="+userid+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1&RESETTYPE=1&PAGETYPE=2";
      $.ajax({
          type: "POST",
          url: "https://api.mobileshop.com/applogin/appforgotpassword.php",
          dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {
          data = ConvertKeysToUpperCase(data);					
          var result = jQuery.parseJSON(JSON.stringify(data));

            if(result.RESPONSECODE == 2 && result.ERRCODE == 118)
            {			    		
              $("#forgeterrorpop1").html("You have entered incorrect OTP.");
              if(result.MESSAGE != ""){
                $("#forgeterrorpop1").html(result.MESSAGE);
              }
              $("#forgotpassword").css("display","none");
              $("#forgeterrorpop1").css("display","block");
              $("#otppageids").css("display","none");
              $("#newpassword").css("display","none");
              $("#successpage").css("display","none");
              $("#forgetotppin").focus();
              return false;	
            }
            else if(result.RESPONSECODE == 1 && result.ERRCODE == 0)
            {
              var otppin = result.REDDISPWD;
              if(result.TOTALID > 1)
              {
                var finalresult = '<form name="matriidtootpfrm"><div class="col-md-12 col-12 login-title-txt"><img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick=loginHideShow("multiids","forgetOtpPageid")> Choose Matri ID</div><div class="col-md-12 col-12 xs-form-pad"><div class="col-md-12 col-12 xs-banner-margin md-none"><img src="http://imgs.mobileshop.com/bmimgs/login/login-otp-mobile-banner.png?v=1"></div><div class="login-label">';
                  for (var i=0; i < result.TOTALIDS ; i++) 
                  { 
                    let domain = result.PROFILEIDS.PROFILEID[i].DOMAIN;
                    let capitalized_domain = domain.replace(/^./, domain[0].toUpperCase()); //converting first letter to uppercase
                    finalresult+='<div class="col-md-12 col-12 float-left pt-0 xs-text-left text-left login-normal-txt"><div class="input-radio-login"><label><input type="radio" class="mr-1" name="selid" value="'+result.PROFILEIDS.PROFILEID[i].MATRIID+'" checked>'+result.PROFILEIDS.PROFILEID[i].MATRIID+'</label><span id="domain" class="ml-2">'+capitalized_domain+'Matrimony</span></div></div>'
                  }
                  finalresult+='<div class="col-md-12 col-12 float-left pt-4 xs-pt-15 login-btn-one"><input type="button" value="CONTINUE" class="login-btn" name="paswdchangeid"  onClick="javascript:return forgetPwdCheckedId();"></div><div class="clear"></div></div></div></form>';

                $("#loading").css("display","none");
                $("#forgotpassword").css("display","none");
                $("#forgetOtpPageid").css("display","none");
                $("#errorpop").css("display","none");			    			
                $("#newpassword").css("display","none");
                $("#redispwd").val(otppin);
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","block");
                loginHideShow('forgetOtpPageid','multiids');
                $("#multiids").html(finalresult);
              }
              else
              {
                $("#otppageid").css("display","none");
                $("#otppageids").css("display","none");
                $("#newpassword").css("display","block");					    			
                $("#errorpop").css("display","none");
                $("#forgotpassword").css("display","none");	  		
                $("#forgetotppin").focus();
                $("#matriid").val(userid);
                $("#redispwd").val(otppin);
                loginHideShow('forgetOtpPageid','newpassword');
              }
            }					    	

          }
        });
    }		
  }

  function resendotp(){
    var matriId = $('#otploginID').val(); 		
    ga('send', 'event','LoginViaOTP-WEB-Mobileshop',' Resent OTP','Click'); 
    ga('tracker1.send','event','LoginViaOTP-WEB-Mobileshop',' Resent OTP','Click',{'nonInteraction': true});

    params ="ID="+matriId+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1";

      $.ajax({
        type: "POST",
        url: "https://api.mobileshop.com/applogin/resend-otp.php",
        dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {
          data = ConvertKeysToUpperCase(data);					
          var result = jQuery.parseJSON(JSON.stringify(data));					
          var message = result.MESSAGE;
          var msg = 'Your OTP has been sent to your registered mobile number.';
          if(result.RESPONSECODE==2 && result.ERRCODE==996)
          {
            $("#errorpop1").css("display","block");
            $("#errorpop1").html(message);
            $("#loginViaOtpHide").css("display","none");	
            $("#otppin").focus();
            return false;
          }
          else if(result.RESPONSECODE==1 && result.ERRCODE==0 || result.RESPONSECODE==2 && result.ERRCODE==72)
          {
            $("#errorpop2").css("display","block");
            $('#errorpop2').html(msg).show().fadeOut(3500, function() { $('#errorpop2'); });
            //$(".success-otp").css("color","#1ba261");
            return false;	
          }	
          else if(result.RESPONSECODE==2 && result.ERRCODE==2)
          {
            $("#forgeterrorpop1").css("display","block");
            $("#forgeterrorpop1").html('You have exceeded the maximum attempts to resend the OTP');
            $("#otppin").focus();
            return false;
          }	    	

        }
      });		
  }

  function checkedid(otp,loginid)
  {
    var checkedId = $('input[name="matriid"]:checked').val();
    if(checkedId)
    {
      params="ID="+checkedId+"&LOGINOTP="+otp+"&LOGINID="+loginid+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1";
      $.ajax({
          type: "POST",
          url: "https://api.mobileshop.com/applogin/otp-login-validation.php",
          data: params,
          dataType: "jsonp",
          crossOrigin: true,
          success: function(data) {	
            var result = jQuery.parseJSON(JSON.stringify(data));

            location.href = result.REDIRECTURL;
          }
        });
    }

  }

  function forgetPwdCheckedId()
  {
    var checkedId = $('input[name="selid"]:checked').val();
    if(checkedId)
    {
      $("#newPasswordBackId").html('<img src="http://imgs.mobileshop.com/bmimgs/login/login-back-arrow.png?v=1" class="align-top" onclick=loginHideShow("newpassword","multiids")>')
      $("#newpassword").css("display","block");
      $("#matriid").val(checkedId);
      $("#forgotpassword").css("display","none");
      $("#errorpop").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      loginHideShow('multiids','newpassword');
    }
  }

  function forgetResendOtp()
  {
    var matriId = $('#fpwdid').val(); 
    params ="ID="+matriId+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1&RESETTYPE=2&PAGETYPE=2";
      $.ajax({
        type: "POST",
        url: "https://api.mobileshop.com/applogin/appforgotpassword.php",
        dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {
          data = ConvertKeysToUpperCase(data);
          var result = jQuery.parseJSON(JSON.stringify(data));

          var message = 'Your OTP has been sent to your registered mobile number.';

          if(result.RESPONSECODE==1 && result.ERRCODE==0)
          {					
            $("#forgeterrorpop2").css("display","block");
            $('#forgeterrorpop2').html(message).show().fadeOut(3500, function() { $('#forgeterrorpop2'); });
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");		
            $("#successpage").css("display","none");			    			
            $("#errorpop").css("display","none");
            $("#forgotpassword").css("display","none");	
            return false;	
          }	
          else if(result.RESPONSECODE==2 && result.ERRCODE==120)
          {					
            $("#forgeterrorpop1").css("display","block");
            $("#forgeterrorpop1").html('You have exceeded the maximum attempts to resend the OTP');
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");					    			
            $("#errorpop").css("display","none");
            $("#forgotpassword").css("display","none");	
            $("#forgotPwdOtpHide").css("display","none");
            $("#forgetotppin").focus();
            return false;
          }	 			    				    	    
        }
      });		
  }

  function forgetCheckedId()
  {
    var checkedId = $('input[name="selid"]:checked').val();
    if(checkedId)
    {
      $("#newpassword").css("display","block");
      $("#matriid").val(checkedId);
      $("#forgotpassword").css("display","none");
      $("#errorpop").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
    }

  }
  function chknewpwd()
  {

    var newpassword = $('#newpass').val(); 
    var confirmpassword = $('#confpass').val(); 
    var MatriId = $('#matriid').val(); 
    var pinno = $('#redispwd').val(); 
    if(newpassword == '')
    {
      $("#forgotpassword").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","block");
      $("#errorpop3").css("display","block");
      $("#errorpop3").html('Enter New Password');
    }
    else if(confirmpassword == '')
    {
      $("#forgotpassword").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","block");
      $("#errorpop3").css("display","none");
      $("#errorpop4").css("display","block");
      $("#errorpop4").html('Enter Confirm Password');
    }
    else if(newpassword != confirmpassword)
    {
      $("#forgotpassword").css("display","none");
      $("#otppageid").css("display","none");
      $("#otppageids").css("display","none");
      $("#newpassword").css("display","block");
      $("#errorpop3").css("display","none");
      $("#errorpop4").css("display","block");
      $("#errorpop4").html('New and Confirm Password are not same');
    }
    else
    {
      $("#errorpop3").css("display","none");
      $("#errorpop4").css("display","none");

      params ="ID="+MatriId+"&NEWPASSWORD="+encodeURIComponent(newpassword)+"&CONFIRMPASSWORD="+encodeURIComponent(confirmpassword)+"&PINNO="+pinno+"&OUTPUTTYPE=2&APPTYPE=300&WEB=1&PAGETYPE=3";
      $.ajax({
        type: "POST",
        url: "https://api.mobileshop.com/applogin/resetpassword.php",
        dataType: "jsonp",
        crossOrigin: true,
        data: params,
        success: function(data) {					
          data = ConvertKeysToUpperCase(data);
          var result = jQuery.parseJSON(JSON.stringify(data));					
          var message = result.MSG;
          if(result.RESPONSECODE==2 && result.ERRCODE==1)
          {
            $("#errorpop3").css("display","none");
            $("#errorpop4").css("display","none");
            $("#errorpop4").css("display","block");
            $("#errorpop4").html('Password does not match');
            return false;
          }
          else if(result.RESPONSECODE==2 && result.ERRCODE==120)
          {
            $("#errorpop3").css("display","none");
            $("#errorpop4").css("display","none");
            $("#errorpop4").css("display","block");
            $("#errorpop4").html('Invalid! Your Password should contain 6-20 characters.');
            return false;
          }
          else if(result.RESPONSECODE==1 && result.ERRCODE==0)
          {
            $("#forgotpassword").css("display","none");
            $("#otppageid").css("display","none");
            $("#otppageids").css("display","none");
            $("#newpassword").css("display","none");
            $("#successpage").css("display","block");
            loginHideShow('resLoginViaOtp','resLoginForm');	
            $("#successpop").css("display","block");
            $('#successpop').html('Password updated successfully').show().fadeOut(4500, function() { $('#successpop'); });
            resetInputValues();	
            $("#successpage").html('<div style="width:390px;"><div style="color:#000" class="hdtxt paddt10 paddb10 txt-center">Your password has been successfully reset</div><div class="txt-center mediumtxt1 paddt10"><a href="https://profile.'+result.DOMAIN+'matrimony.com/login/login.php" style="background: #ff7c0b;border: 1px solid #ff7c0b;border-radius: 3px;display: block;margin: 0 auto;padding: 7px 28px;text-decoration: none;width: 40px;" class="smalltxt2 boldtxt clr6" onclick="loginTrack();">Login</a></div></div>');
            return false;	
          }		    		

        }
      });		
    }
  }
  </script>
  <!-- Forgot Password End -->

  <script>
  function myFunction(x) {
  x.classList.toggle("login-eye-on");
  }
  $('.icon').hover(function () {
    $('.password').attr('type', 'text');
  }, function () {
    $('.password').attr('type', 'password');
  });

  function showHidePwd(id){
    var input = $("#"+id);
    if (input.attr("type") === "password") {
      input.attr("type", "text");
    } else {
      input.attr("type", "password");
    }
  }
  </script>	 
