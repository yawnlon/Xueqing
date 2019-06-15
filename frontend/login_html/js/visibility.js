
<!DOCTYPE html>

<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
    <title>

	AxShare - Prototype Password

</title>
    <link href="/Content/Site.css" rel="stylesheet" type="text/css" />
    <link href="/Content/axStyles.css" rel="stylesheet" type="text/css" />

        <link rel="stylesheet" href="https://www.axure.com/content/nexa_lightregular.css" type="text/css" />
        <link rel="stylesheet" href="https://www.axure.com/content/proxima_nova.css" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" />
    

    <script type="text/javascript">
            AXSHARE_HOST_URL = 'http://app.axure.cloud';
            AXSHARE_HOST_SECURE_URL = 'https://share.axure.com';
            ACCOUNT_SERVICE_URL = 'http://accounts.axure.com';
            ACCOUNT_SERVICE_SECURE_URL = "https://accounts.axure.com";
            AXSHARE_ON_PREM = false;
    </script>

    <script src="/Scripts/jquery-1.7.1.min.js" type="text/javascript"></script>
    <script src="/Scripts/jquery.axDialog.js" type="text/javascript"></script>
    <script src="/Scripts/sha512-min.js" type="text/javascript"></script>
    <script src="/Scripts/axshareUtils.js" type="text/javascript"></script>

    <script src="/Scripts/axPage.js" type="text/javascript"></script>
    


        <script type="text/javascript">
 (function (i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                    (i[r].q = i[r].q || []).push(arguments);
                }, i[r].l = 1 * new Date(); a = s.createElement(o),
                    m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m);
            })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

            ga('create', 'UA-586346-7', 'axure.com', { 'storage': 'none' });
            ga('set', 'anonymizeIp', true);
            ga('send', 'pageview'); 
            $axshare.autoLogin = false;
            if ($axshare.axAccountJsAvailable) {
                $(document).ready(function () {
                    $axshare.auth(function (response) {
                        if ($axshare.autoLogin && response.success) {
                            $axshare.setAuthCookie(response.authToken);
                            window.location.href = 'https://app.axure.cloud/app' || $axshare.urlPaths.fsmanage;
                        }
                    });
                });
            }
        </script>
    

    <meta name="robots" content="NOINDEX, NOFOLLOW"/>


</head>



<body>
    <div class="page">

        <div id="header">
            <div id="headerContents" class="responsiveWidth">

                <div id="mainLogo">
                            <a href="/"><img src="/images/logo_120.svg" alt="Axure Software Solutions" /></a>
                </div>

                <div id="profileRightSide">


                    <div id="topNav">
                    </div>
                </div>
            </div>
        </div>

        <div id="core">
            <div id="coreContents" class="responsiveWidth">
                



    <script defer="defer" type="text/javascript">
    <!--
        //Isolate Javascript scope
        (function () {
            $(document).ready(function() {
                $axpage.hideProfileHeader(true);
                $axpage.hidePageTabNav(true);
                $('#header').css('background-color', '#FFFFFF');

                var pathCookieName = 'prototypeRequestPath';

                function getPathCookieValue() {
                    var i, x, y, ARRcookies = document.cookie.split(";");
                    for (i = 0; i < ARRcookies.length; i++) {
                        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
                        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
                        x = x.replace(/^\s+|\s+$/g, "");
                        if (x == pathCookieName) {
                            return decodeURIComponent(y);
                        }
                    }

                    return null;
                }

                function deletePathCookie() {
                    var date = new Date();
                    date.setTime(date.getTime() + (-1 * 24 * 60 * 60 * 1000));
                    var expires = '; expires=' + date.toGMTString();
                    document.cookie = pathCookieName + '=0' + expires + '; path=/';
                }

                $('#loginForm').submit(function () {
                    $('#errorMessage').empty();

                    var form = $(this);
                    var url = form.attr('action');

                    var dataToSend = {
                        Password: hex_sha512(form.find('#Password').val()),
                        currenthost: window.location.hostname
                    };

                    var pathCookieValue = getPathCookieValue();
                    if (pathCookieValue != null) {
                        dataToSend['path'] = pathCookieValue;
                    }

                    //If accessing a prototype via https, make cookie secure
                    var cookieSuffix = window.location.href.indexOf('https://') != -1 ? '; secure' : '';

                    $axshare.secureSubmit({
                        url: url,
                        data: dataToSend,
                        success:
                        function (response) {
                            if (response.success) {
                                //delete the path cookie, set the auth cookie, then redirect to the prototype
                                deletePathCookie();
                                if(response.redirecturl.indexOf('/proto/tokenset') == -1) document.cookie = response.data.Vars.authCookieString + '; path=/' + cookieSuffix;
                                window.location.replace(response.redirecturl + window.location.hash);
                            } else {
                                $('#errorMessage').text(response.message);
                            }
                        }
                    });

                    return false;
                });

                /* Watermark (aka hint) handler for login/signup Password fields */
                $('#Password').addClass("watermark").val("Enter Project Password").focus(function () {
                    if ($(this).val() === "Enter Project Password") {
                        $(this).removeClass("watermark").val("");
                        $(this).prop('type', 'password');
                    }
                }).blur(function () {
                    if ($(this).val() === "") {
                        $(this).val("Enter Project Password").addClass("watermark");
                        $(this).prop('type', 'text');
                    }
                });

                /* Pressing enter in input field event handler */
                $('#Password').keypress(function (e) {
                    if (e.which === 13) {
                        $('#logInButton').click();
                    }
                });

                $('.loginfield').focus();
            });
        })();
    //-->
    </script>
    
    <div id="prototypeLoginPageHeader" class="pageHeader" style="display: none;"></div>
    
    <div id="prototypeLoginPageContents" class="pageContents" style="padding-top: 0px; display: block; margin: auto; width: 70%;">
        <form id="loginForm" action="/prototype/dologin/B9ZVTW" method="POST" style="border: solid 1px #EDEDED; padding: 46px 60px; width: 840px; ">
            
            <h1 style="margin: 0 0 35px 2px; color: #414141;">Please enter the password for this project</h1>    

            <div class="userLoginBox">
                <div class="loginrow">
                    <input class="loginfield" id="Password" name="Password" style="width: 100%; font-size: 24px; height: 50px;" type="text" value="" />
                </div>

                <div style="text-align:right; margin:6px 0px 0px 0px;">
                    <div class="axGreenRoundedBtn loginsubmit" style="display: inline-block; font-size: 22px; height: 65px; line-height: 65px; width: 100%;" onclick="javascript:$(this).parents('form').submit();">VIEW PROJECT</div>
                </div>

                <div id="errorMessage" class="validation-summary-errors" style="text-align:center; margin-top: 10px;"></div>
            </div>
        </form>
    </div>


                
            </div>
        </div>

            <div id="footer">
                <div id="footerContents" class="responsiveWidth">
                    <div id="rpCopyright">
                        <div id="rpLogo"></div>
                        <div id="copyrightInfo">
                            <span>
                                &copy; 2002-2019 Axure Software Solutions, Inc.<br />
                                All rights reserved. Axure&copy; is a registered trademark of Axure Software Solutions, Inc.
                            </span>
                        </div>
                    </div>
                        <div id="footerLinks">
                            <div id="axureLinks" style="width: 225px;">
                                <div id="axureLinksLabel">AXURE</div>
                                <div id="axureLinks0">
                                    <a href="http://www.axure.com/" target="_blank">HOME</a><br />
                                    <a href="http://www.axure.com/#a=features" target="_blank">FEATURES</a><br />
                                    <a href="http://www.axure.com/business-case" target="_blank">BUSINESS CASE</a><br />
                                    <a href="http://www.axure.com/support" target="_blank">SUPPORT</a>
                                </div>
                                <div id="axureLinks1">
                                    <a href="http://www.axure.com/company" target="_blank">COMPANY</a><br />
                                    <a href="http://www.axure.com/download" target="_blank">DOWNLOAD</a><br />
                                    <a href="http://www.axure.com/buy" target="_blank">PURCHASE</a><br />
                                    <a href="http://www.axure.com/support/reference/axure-share-basics" target="_blank">SHARE GUIDE</a>
                                </div>
                            </div>
                            <div id="resourceLinks" style="width: 150px;">
                                <div id="resourceLinksLabel">RESOURCES</div>
                                <div id="resourceLinks0">
                                    <a href="https://share.axure.com/" target="_blank">AXURE SHARE</a><br />
                                    <a href="https://www.axure.com/portal/user" target="_blank">AXURE PORTAL</a><br />
                                    <a href="http://www.axure.com/c/blog/" target="_blank">AXURE BLOG</a><br />
                                    <a href="http://www.axure.com/c/forum.php" target="_blank">AXURE FORUM</a><br />
                                </div>
                            </div>
                            <div id="emailLinks" style="width: 150px;">
                                <div id="emailLinksLabel">EMAIL</div>
                                <div id="emailLinks0">
                                    <a href="mailto:sales@axure.com">SALES@AXURE.COM</a><br />
                                    <a href="mailto:contactus@axure.com">CONTACTUS@AXURE.COM</a><br />
                                    <a href="mailto:support@axure.com">SUPPORT@AXURE.COM</a>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
        

    </div>
</body>
</html>
