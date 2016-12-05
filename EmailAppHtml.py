# -*- coding: utf-8 -*-
import email.message
import smtplib


msg = email.message.Message()
msg['Subject'] = 'foo'
msg['From'] = 'gdghanoi2@gmail.com'
msg['To'] = 'whiteroses995@gmail.com'

body = '''

<head>
  <meta charset="utf-8">
</head>
<div id=":1ma" class="a3s aXjCH m157ded1174c78463"><div class="adM">

</div><u></u>
<div dir="" style="border:0;font-family:Arial;font-weight:normal;margin:0;padding:0;width:100%" width="100%">
    <div style="height:0px;font-size:0px;max-height:0px;min-height:0px;line-height:0px;width:100%;color:#fff;display:none">Google Devfest 2016</div>

	<table class="m_-288105649877653498bigger_wrapper m_-288105649877653498flexible" width="800" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Arial,sans-serif;font-weight:normal;margin:0 auto;max-width:800px;min-width:800px">
        <tbody>
          <tr>
            <td class="m_-288105649877653498bigger_wrapper_header m_-288105649877653498flexible" style="border-collapse:collapse;margin:0;max-width:800px;min-width:800px">

                <table width="600" class="m_-288105649877653498header_wrapper m_-288105649877653498flexible" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:0 auto;width:600px">
                    <tbody>
                      <tr>
                        <td style="border-collapse:collapse">

                            <table width="auto" class="m_-288105649877653498logo_holder" align="left" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:roboto,arial;font-weight:500;width:auto">
                                <tbody>
                                  <tr>
                                    <td class="m_-288105649877653498logo_holder_td" style="border-collapse:collapse;padding-bottom:25px;padding-top:25px">
                                        <a href="http://devfesthanoi.com/"><img src="https://lh3.googleusercontent.com/V3URawn9tOWBeOeZlAJm37wYjVNG5iwNnlOjR-BKD8wKOIBpfe6OpB3_9s_7wULLPzcFo9pox4niYS9oG4IoBN56FAMXWv-6813NmMVmDZTkCVqhMI7olIT1xyfryYj_Uf1zVGLymrmSOa1NRfiTMB0qCGJ-IWdA8kd-30ovuCUNdEtBa1QVDtGu_tuVOtvTcvP8fl9VoSmX5y3SzvNkbJBHFkp0H-IiDjtSTY2wKq6DezT6HFspa4ITV9YOA0wo8cYeROyJad2Js2gdIgCl2J1EXrCmUxLC5EWMrmSNpj-8dydE34D-lZzz9N23vSMuf_An-o__9lJ0q49nZupYGZN3khawEE4r2zrgJVFxZsuvdEcWoVrcfAgrjq9QVtEcS96XQMhe5WYJ17nP3fsU9GOPEYJwqa4Dy1zYRmaMFSdJz6OU9NGAogM5DDXaMZpf33Iv1_Ycl-inLEAyMVQpiBNj3LTKTvgN1opN9OsNTiCGTqDe_tk-BITjhjfscIQk5CPTKAiQf8LPhu5vi1sat_D5Qp7ieH-FfG8Rf_tWmMmXlapVmEiMOWYzBl6a3JO3T4OXQZtIEFzESWGy8IWJTzavULovA1JzJXHdytL0C12EGk6C=w1366-h378-no" width="160" alt="GDG Hanoi" style="outline:none;text-decoration:none" class="CToWUd"></a>
                                    </td>
                                  </tr>
                                </tbody>
                            </table>

                            <table width="auto" class="m_-288105649877653498logo_right_holder" align="right" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Roboto,arial;font-weight:500;width:auto">
                                <tbody>
                                  <tr>
                                    <td class="m_-288105649877653498logo_right_holder_td" style="border-collapse:collapse;padding-right:0;padding-top:34px">
                                        <table class="m_-288105649877653498logo_right_holder_inner" style="border-collapse:collapse;font-family:roboto,arial;font-weight:500;width:auto" cellpadding="0" cellspacing="0" width="auto">
                                            <tbody>
                                              <tr>
                                                <td style="border-collapse:collapse;color:#FBC02D;font-size:14px;font-family:roboto,arial;font-weight:500"><a href="http://devfesthanoi.com/" style="color:#F4B400;font-size:14px;text-decoration:none" target="_blank" >HOME</a>
                                                </td>
                                              </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                  </tr>
                                </tbody>
                            </table>
                        </td>
                      </tr>
                    </tbody>
                </table>

            </td>
          </tr>

          <tr>
            <td class="m_-288105649877653498bigger_wrapper_body m_-288105649877653498flexible" bgcolor="#6b6b6b" style="border-collapse:collapse;margin:0;max-width:800px;min-width:800px">
            	   <table width="600" class="m_-288105649877653498body_content_wrapper m_-288105649877653498flexible" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:0 auto;width:600px">
                    <tbody>
                        <tr>
                  	       <td class="m_-288105649877653498sub_header" style="border-collapse:collapse;color:#ffffff;font-family:Roboto,arial;font-size:14px;font-weight:500;line-height:16px;padding-bottom:22px;padding-top:20px">
                  	       	Newsletter | November 2016
                        	 </td>
                        </tr>
            	       </tbody>
                </table>
            </td>
          </tr>


          <tr>
              <td bgcolor="#035cdb" class="m_-288105649877653498banner_container" style="background-image:url(https://lh3.googleusercontent.com/TLRyLFdsZH_yPpu7jPMma28ZH0Wds2_HdABRzpfAPCp5kw2xNkuwmOwLX2jRuHjED42sSXGHDMQAEmhW4wJfuuxmZZodjhkuLl2krbVY5ENKVZZdrvrlvUPxblXCFrmCwnWYIzQ-jCn76Fj0S8T8jOF9IRhnxCgoC_r__Fgqw5MpMOSC2mvGWJxTo7HIt06BccOSoCJXvXWkEAarp0dvM68l4D59fS-_I-rUjGX0tDZs1pAlLVGs6MZgJFMeLHTCytDmXc4jT_bS92RJZ7BBkGVJsr5yAW9PCl_sOQ5dvmhh8vJKVjbvAnXF9tMJ_d2OL2tW0bWABUfAb4ePsI-nLPbYGuXzXEHREX3vv67MtDk_phvSh9tdNttXFnMyahWuztRXQbcfEK913fDbcwFE6DCZWv8eQb9ImAiRyax_I4X2Y-_b3C5wAvYowDM_vpF15xxunpDBusWw2asZWcCdjymQULpvTHTJ5m3sQyGlH-9G2gnlk-jIIVxlU7EttMiGzkegVX0FPxLi7hEVNVyQVVTqr4WjrE2tL7hxEN1bU2PYgl5YkKUA6-ldIP-oTRhClMj53XTJI-9f9Yc9FcJA-eMKiWBsYkojnjvJHTK-_qJUUlWt=w800-h600-no);background-repeat:no-repeat;border-collapse:collapse;display:block;margin:0;padding:0;height:590;width:800" width="800" height="590" valign="top">
                  <div id="m_-288105649877653498MainBG" style="height:auto;margin:0 auto;max-width:600px;width:100%" class="m_-288105649877653498holder_wrap_inner m_-288105649877653498flexible" height="" width="100%">
          	        <table align="center" border="0" cellpadding="0" cellspacing="0" class="m_-288105649877653498holder_wrap_inner m_-288105649877653498flexible" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:auto;max-width:600px;width:600px" width="600">
                        <tbody>
                          <tr>
                              <td align="center" style="border-collapse:collapse;padding-top: 310px">
                                <table style="margin:auto;border-collapse:collapse;border-radius:3px;color:#ffffff;font-family:Roboto,Arial;font-weight:normal" height="42" align="center" bgcolor="#ffffff" cellpadding="0" cellspacing="0">
                                    <tbody>
                                      <tr>
                                        <td style="border-collapse:collapse">
                                          <a style="background-color:#ffffff;border-bottom-left-radius:5px;border-bottom-right-radius:5px;border-color:#ffffff;border-radius:5px;border-style:solid;border-top-left-radius:5px;border-top-right-radius:5px;border-width:10px 17px 10px 17px;color:#F4B400;display:inline-block;font-family:Roboto,Arial;font-size:14px;font-weight:500;line-height:18px;margin:0;text-align:center;text-decoration:none;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 30px 0 rgba(0, 0, 0, 0.15);" href="http://devfesthanoi.com/register/" bgcolor="#ffffff" align="center" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=vi&amp;q=https://www.google.com/appserve/mkt/p/wrAntdI6Rf7Yfw0T8LKcHC7m2sx93rOfB9ZZLdFWEIMmLOKbQyNBpwpCHkiKPUJ4rVtXSwTWg7fLBy8bCGFKKdP8UVJWWdNg6zwwouBMDVe1oeEmsdhLONnxfqv1wuVYIVFENqZNxHjROEKYlEQ8wNXBwJqkvUw%3D&amp;source=gmail&amp;ust=1477973572317000&amp;usg=AFQjCNGx2dSNYWoKxTYzJQIBYbBc3yqwGQ">
                                             <span align="center" style="display:block;padding-left:8px;padding-right:8px;padding-top:5px; padding-bottom: 5px">REGISTER NOW</span>
                                          </a>
                                        </td>
                                      </tr>
                                    </tbody>
                                </table>
                              </td>
                          </tr>
                        </tbody>
                    </table>
                  </div>
              </td>
          </tr>


          <tr>
            <td class="m_-288105649877653498bigger_wrapper_body m_-288105649877653498flexible" style="border-collapse:collapse;margin:0;max-width:800px;min-width:800px;background-color:#FFFEED">
          	  <table width="600" class="m_-288105649877653498body_content_wrapper m_-288105649877653498flexible" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:0 auto;width:600px">
              </table>
                <table width="600" class="m_-288105649877653498body_content_wrapper m_-288105649877653498flexible" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:url(https://fonts.googleapis.com/css?family=Roboto:400,700,300,500&subset=vietnamese,latin-ext);font-weight:normal;margin:0 auto;width:600px">
                  <tbody>
                    <tr>
                      	<td class="m_-288105649877653498body_heading m_-288105649877653498flexible m_-288105649877653498body_heading_text" style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:24px;font-weight:bold;line-height:32px;padding-bottom:30px;padding-top:37px;display: flex;
                        align-items: center;justify-content: center">
                      		Sự kiện Google Devfest 2016
                      	</td>
                    </tr>

                    <tr>
                    	 <td class="m_-288105649877653498body_text m_-288105649877653498flexible" style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:regular;line-height:24px;padding-bottom:11px;padding-top:1px;text-align: justify">
                    		<p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:regular;line-height:10px;padding-left:20px;padding-top:10px;">
                        Chào (.......),</p>
                        Bạn được mời đăng ký tham dự sự kiện <span style="font-weight:bold">Google Devfest 2016</span>.
                        Tiếp nối sự  thành công của Google I/O Extended 2016 trong thời gian vừa qua, Google Developers Group Hanoi (GDG Hanoi) hân hạnh được tiếp tục đem đến sự kiện <span style="font-weight:bold">Google Developers Festival 2016(Google Devfest 2016)</span> dành riêng cho các lập trình viên cũng như các công ty khởi nghiệp về công nghệ.</br></br>
                        Là một sự kiện cộng đồng miễn phí, Google DevFest 2016 đem đến cơ hội tiếp xúc và trải nghiệm những công nghệ, ngôn ngữ mới nhất hiện nay như Machine Learning, Go, Nodejs, Python cùng các diễn giả đến từ Google và các công ty công nghệ lớn ở Việt Nam. Đồng thời, sự kiện cũng là nơi giúp người tham dự tìm hiểu và có thêm kiến thức hỗ trợ đa ngành về các lĩnh vực như quảng cáo và kinh doanh cũng như cơ hội trải nghiệm các  sản phẩm công nghệ cùng Google.</br></br>
                        Chuỗi sự kiện của Google DevFest đã được tổ chức thành công trên nhiều quốc gia như Pháp, Brazil, Ukraine bởi Google Developer Group của Google. Tại Việt Nam, sự kiện Google DevFest 2016 hứa hẹn sẽ mang lại kiến thức bổ ích nhất tới lập trình viên và chúng tôi hi vọng sẽ được gặp bạn tại sự kiện.</br></br>
                        Thông tin chi tiết về sự kiện:</br>
                        <p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:bold;line-height:20px;padding-left:20px">- Thời gian: 1:00PM - 5:30PM ICT, Thứ Bảy ngày 26 tháng 11 năm 2016.</p>
                        <p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:bold;line-height:20px;padding-left:20px">- Địa điểm: Học viện Bưu Chính Viễn Thông - Km10, Đường Nguyễn Trãi, Quận Hà Đông, Hà Nội.</p>
                        Link đăng ký: <a href="http://devfesthanoi.com/register">http://devfesthanoi.com/register</a>.</br>
                        Tham khảo thông tin:<a href="https://www.facebook.com/GDGhanoi">https://www.facebook.com/GDGhanoi</a>.
                        <p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:bold;line-height:20px;padding-left:20px">
                        Diễn giả từ Google:</br></p>
                        1. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Robert Kubis</a> - Developer Relations Program Manager, South & Southeast Asia, Google</br>
                        2. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Ian Lewis</a> - Developer Advocate Google for Google Cloud</br>
                        3. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Allen Day</a> - Evangelist (Genomics / Cloud)</br>
                        4. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Tu Pham</a> - Google Developer Expert(Cloud)</br>
                        5. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Trung Quang Dinh</a> - Google Developer Expert (Web Technologies)</br>
                        6. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Hien Gaby</a> - Sr. Strategist, Account Manager - Google Singapore</br>
                        7. <a href="http://devfesthanoi.com/speakers/" style="text-decoration:none">Van Vuong</a> - Online Publishing Group</br>
                        (Updating...)
                        <p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:regular;line-height:20px;padding-left:430px">
                        Trân trọng,</p>
                        <p style="border-collapse:collapse;color:#6b6b6b;font-family:Roboto,arial;font-size:14px;font-weight:bold;line-height:40px;padding-left:425px;padding-bottom: 15px">
                        The X Team</p>

                    	 </td>
                    </tr>
                  </tbody>
              </table>
            </tr>

            <tr>
            <td class="m_-288105649877653498bigger_wrapper_body m_-288105649877653498flexible" bgcolor="#6b6b6b" style="border-collapse:collapse;margin:0;max-width:800px;min-width:800px">
                 <table width="600" class="m_-288105649877653498body_content_wrapper m_-288105649877653498flexible" align="center" cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:0 auto;width:650px">
                    <tbody>
                      <td class="m_-288105649877653498logo_holder_td" style="border-collapse:collapse;padding-top:25px">
                        <img src="https://lh3.googleusercontent.com/WOkT4d5ahCmPKbs9JMPsC6fVrXh6l6j56VTxr4pD5zjYHIw_CKpETnSyYgMq9gwFT6mBHiRwpswLwNn7hMudkUAx4Qbbo0eHEyu7jPiQyB23h_10c-inO9u0XohnjBymOW4HDOsVO8qwfb9b_9k_YaV9N20EaS-V725v-Hj66VKVDz3R1yVREK3X4XcRmKdgDBCJ1LYGZlRxdhbC32kvjbtXs_CpZTpkmpsvK2JnDUTiTHWG_Y_oWsZ2LDV6-HudVun6vAw7H-zVETB8mQcPUzVwG_Sp5WXNUtWKOtkXCEyBp2Idz45f_UXCYNDG7QV_hCz5F5xAw_8niMrNw1xMfEm8b8XiBY-OgNjzCcCaHMPvROoj1WUtFWJljdTYlqVXUiQB7ZhPUMYi4mel6sFt6tmmXm6rx5utRP-UOI8oliqwouYB9SdDIgkR_G5ZRUVGkljbFRjSsDh9yZOfDZaOc4TDbp_HX9PPUrYBe719fDm7mP1UVZOhxHn66oryDEIG-SHCblDr1rNgQvWYnWbATLRQ0CYIh67yuDbj-zH4DWHZ0onGd4wwv2C1tbQ--DiF4P3r2Qg_xSqC8oEBi23gJ2kpwhaSNg0hI0Adst40x0tDlKso=w283-h65-no" width="100" alt="GDG Hanoi" style="outline:none;text-decoration:none" class="CToWUd">
                      </td>
                        <tr>
                           <td class="m_-288105649877653498sub_header" style="border-collapse:collapse;color:#cbcbcb;font-size:12px;line-height:18px;padding:10px 0 40px 0;padding-bottom:5px">
                            We work directly with Google Developer Relation Team</br>
                            to bring awesome events to developers in Ha Noi
                           </td>
                        </tr>
                        <tr>
                           <td class="m_-288105649877653498sub_header" style="float: left; border-collapse:collapse;color:#cbcbcb;font-size:12px;line-height:18px;padding:10px 0 40px 0;padding-bottom:5px">
                            Contact us:</br>
                            gdghanoi@gmail.com
                           </td>
                        </tr>
                       <tr>
                          <td class="m_-288105649877653498social_icons_container m_-288105649877653498flexible" style="border-collapse:collapse;padding:10px 0 25px 0">
                            <table class="m_-288105649877653498social_icons_container_inner" cellspacing="0" cellpadding="0" border="0" width="210" align="left" style="border-collapse:collapse;font-family:Roboto,Arial;font-weight:normal;margin:0 auto;width:100px">
                                <tbody>
                                   <td class="m_-288105649877653498logo_holder_td" width="34" style="border-collapse:collapse"><a href="https://plus.google.com/u/0/+GdghanoiOrg"><img src="https://ci6.googleusercontent.com/proxy/-hSbtXd5mUcsZlb-sniKdeYLk3QCmXv5sdujYyjK_WvuSH7hYUbTOAXT2t8qHAl1z2zGxbXeGdkb4ffFcKkchLm4rkr88Nw58S1G9eIRG-OAIfzY9FnjiaG7=s0-d-e1-ft#https://services.google.com/fh/files/emails/gcp_newsletter_gplus.png" width="33" alt="Gmail" style="outline:none;text-decoration:none" class="CToWUd"></a>
                                    </td>
                                    <td class="m_-288105649877653498logo_holder_td" width="34" style="border-collapse:collapse"><a href="https://www.facebook.com/GDGhanoi"><img src="https://ci3.googleusercontent.com/proxy/UoK_rTj07TCkBEZu-OIWm9M84YFXWs7yWEprz8vwTPgn8wXCR6Q7T3YcLx6naUWPEooh6tcPwTqAjVCLpvrQdEr6U2Lt4xSEt6Fkww=s0-d-e1-ft#http://services.google.com/fh/files/emails/fb_july.png" width="33" alt="facebook" style="outline:none;text-decoration:none" class="CToWUd"></a>
                                    </td>
                                </tbody>
                            </table>
                          </td>
                        </tr>
                     </tbody>

                </table>
            </td>
          </tr>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>


     <img height="1" src="https://ci5.googleusercontent.com/proxy/R6MKX7g3YM07PN6mLnLyMknwIKeVapnttyFpC3YRRiu5QtPAGW06RD2kvqb6hvuVV6jTlCA2MFxff6UkBJmAKYhnWy7r6vXYxm5SXmmP_wKXtdzQYlxkzbB6oq0Sag=s0-d-e1-ft#https://www.google.com/appserve/mkt/img/qZI4PI0KSfBq0wVUQ9xdMeRbhqN5.gif" width="3" class="CToWUd">
      <div class="yj6qo"></div>
      <div class="adL"></div>
      <div class="adL"></div>





'''

msg.add_header('Content-Type','text/html')
msg.set_payload(body)

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login('gdghanoi2@gmail.com',
        'xteam123')
s.sendmail(msg['From'], [msg['To']], msg.as_string())