<template>
<el-container :style="bgImg">
<el-row type="flex" class="row-bg" justify="center">
  <el-col :span="12">
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">

      <!-- <div class="title-container">
        <h3 class="title">Login Form</h3>
      </div> -->
      <el-row>
        <div id="u18" class="ax_default image">
          <img id="u18_img" class="img" :src="log_img">
        <!-- <div id="u2_text" class="text ">
          <p><span style="text-decoration:none;" class="login_title">学清书院单词速记</span></p>
        </div> -->
        </div>
      </el-row>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="mobile" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="请输入手机号码"
          type="text"
          tabindex="1"
          autocomplete="off"
        />
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="email" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            :type="text"
            placeholder="请输入短信验证"
            tabindex="2"
            autocomplete="off"
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleLogin"
          />

          <!-- <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span> -->
          <el-button type="text" class="show-pwd" style="font-size:0.8em;color:#02A7F0" :disabled="codeDisabled" @click.native.prevent="sendCode()">
            {{ codeMsg }}
          </el-button>
        </el-form-item>
      </el-tooltip>
      <el-row class="login_font lgn_row_top">
        <!-- <el-col :span="12"><div class="grid-content bg-purple left"><el-checkbox v-model="checked" />&nbsp;记住登录状态</div></el-col> -->
        <el-col :span="12" :offset="12"><div class="grid-content bg-purple-light right f12"><router-link to="/reset">忘记密码？</router-link></div></el-col>
      </el-row>
      <el-button :loading="loading" type="primary" class="u3_div" @click.native.prevent="handleLogin">登录</el-button>
      <el-row class="login_font lgn_row_bottom">
        <el-col :span="12"><div class="grid-content bg-purple left f12"><router-link to="/login">密码登录>></router-link></div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple-light right f12"><router-link to="/signup">注册新账号>></router-link></div></el-col>
      </el-row>

      <!--<div style="position:relative">
        <div class="tips">
          <span>Username : admin</span>
          <span>Password : any</span>
        </div>
        <div class="tips">
          <span style="margin-right:18px;">Username : editor</span>
          <span>Password : any</span>
        </div>
         <el-button class="thirdparty-button" type="primary" @click="showDialog=true">
          Or connect with
        </el-button>
      </div>-->
    </el-form>

    <el-dialog title="Or connect with" :visible.sync="showDialog">
      Can not be simulated on local, so please combine you own business simulation! ! !
      <br>
      <br>
      <br>
      <social-sign />
    </el-dialog>
  </div>
    </el-col>
</el-row>
<Footer/>
</el-container>
</template>

<script>
import log_img from '@/assets/front/logo-part3.png'
// import { validUsername, isPhone } from '@/utils/validate'
import SocialSign from './components/SocialSignin'
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
export default {
  name: 'Login',
  components: { Footer:require('@/views/common/footer').default},
  data() {
    var validatePassword = (rule, value, callback) => {
      value = value + ''
      if (value === '') {
        callback(new Error('请输入短信验证码'))
      } else if (value.length!=6) {
        callback(new Error('短信验证码格式错误'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        // username: '13051975811',
        // password: 'super_admin',
        username: '',
        password: '',
        code: ''
      },
      loginRules: {
        username: [
          { required: true, trigger: 'blur', message: '请输入手机号码' },
          { pattern: /^((1[3,5,8][0-9])|(14[5,7])|(17[0,5,6,7,8])|(19[7]))\d{8}$/, message: '请检查手机号是否正确', trigger: 'blur' }
        ],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      log_img: log_img, // + '?' + new Date(),
      checked: false,
      bgImg: 'background-image:url(' + require('@/assets/front/bg-01.png') + ');background-repeat: repeat;background-color: #02a7f0;',
      message: '',
      // 是否禁用按钮
      codeDisabled: false,
      // 倒计时秒数
      countdown: 60,
      // 按钮上的文字
      codeMsg: '发送验证码',
      // 定时器
      timer: null
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    },
    'loginForm.password': {
      deep: true,
      handler(n, o) {
        this.loginForm.code = n
      }

    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock({ shiftKey, key } = {}) {
      if (key && key.length === 1) {
        if (shiftKey && (key >= 'a' && key <= 'z') || !shiftKey && (key >= 'A' && key <= 'Z')) {
          this.capsTooltip = true
        } else {
          this.capsTooltip = false
        }
      }
      if (key === 'CapsLock' && this.capsTooltip === true) {
        this.capsTooltip = false
      }
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    sendCode() {
      let self = this
      this.$refs.loginForm.validateField('username', (error) => {
        if (!error) {
          // 验证码60秒倒计时
          if (!this.timer) {
            axios
              .post('/api/v1/sms/send', { 'mobile': this.loginForm.username, 'template': 'SMS_167655083' })
              .then(response => {
                this.codeDisabled = true
                this.timer = setInterval(() => {
                  if (this.countdown > 0 && this.countdown <= 60) {
                    this.countdown--
                    if (this.countdown !== 0) {
                      this.codeMsg = '重新发送(' + this.countdown + ')'
                    } else {
                      clearInterval(this.timer)
                      this.codeMsg = '重发验证码'
                      this.countdown = 60
                      this.timer = null
                      this.codeDisabled = false
                    }
                  }
                }, 1000)
                // this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
                // this.loading = false
                self.message && self.message.close()
                self.message = Message({
                  message: '验证码发送成功',
                  type: 'sucess',
                  duration: 5 * 1000
                })
              })
              .catch(error=>{
                self.message && self.message.close()
                self.message = Message({
                  message: error.response.data.detail,
                  type: 'error',
                  duration: 5 * 1000
                })
              })
          }
        }
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        console.log(valid)
        if (valid) {
          // this.loading = true
          // axios
          // .post('/api/account/login',{'mobile':this.loginForm.username,'password':this.loginForm.password})
          // .then(response => {
          //   this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
          //   this.loading = false
          // })
          // .catch(function (error) { // 请求失败处理
          //     error => {
          //       Message({
          //         message: error.message,
          //         type: 'error',
          //         duration: 5 * 1000
          //       })
          //       this.loading = false
          //     }
          // })
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
              this.loading = false
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
    // afterQRScan() {
    //   if (e.key === 'x-admin-oauth-code') {
    //     const code = getQueryObject(e.newValue)
    //     const codeMap = {
    //       wechat: 'code',
    //       tencent: 'code'
    //     }
    //     const type = codeMap[this.auth_type]
    //     const codeName = code[type]
    //     if (codeName) {
    //       this.$store.dispatch('LoginByThirdparty', codeName).then(() => {
    //         this.$router.push({ path: this.redirect || '/' })
    //       })
    //     } else {
    //       alert('第三方登录失败')
    //     }
    //   }
    // }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */
$bg:#283443;
$light_gray:#fff;
$cursor: #fff;
$more_gray:#999999;
$mycursor:#666;

svg{
  font-size: 18px;
}
@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}
/* reset element-ui css */
.login-container {
  .f12{
    font-size: 12px;
  }
  .el-input {
    display: inline-block;
    height: 42px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      // padding: 12px 5px 12px 15px;
      color: $more_gray;
      height: 40px;
      caret-color: $mycursor;
      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px white inset !important;
        -webkit-text-fill-color: $more_gray !important;
      }
    }
  }
  .el-form-item {
    border: 1px solid #dbdbdb;
    background: transparent;
    border-radius: 5px;
    color: #454545;
    margin-left: 25px;
    margin-right:25px;
  }
  .el-form-item:focus-within {
      border:1px solid rgba(2, 167, 240, 1);
    }
}
</style>

<style lang="scss" scoped>
$bg:rgba(105, 43, 128, 1);
$dark_gray:#889aa4;
$light_gray:#eee;
.el-container{
    width:100%;
    height: 100%;
  }
.login-container {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  cursor:black;
  // .login-form {
  //   position: relative;
  //   width: 520px;
  //   max-width: 100%;
  //   padding: 160px 35px 0;
  //   margin: 0 auto;
  //   overflow: hidden;
  // }
  .left {
    text-align: left
  }
  .right{
    text-align: right
  }
  .u3_div {
    border-width: 0px;
    // position: absolute;
    left: 0px;
    top: 0px;
    width: 300px;
    height: 36px;
    background: inherit;
    background-color: rgba(2, 167, 240, 1);
    border: none;
    border-radius: 3px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    // font-family: '寰蒋闆呴粦 Regular', '寰蒋闆呴粦';
    font-weight: 400;
    font-style: normal;
    font-size: 18px;
    color: #FFFFFF;
  }
  .u3_div:hover{
    background-color: rgba(2, 167, 240, 0.8);
  }
  .u1_div {
    border-width: 0px;
    position: absolute;
    left: 0px;
    top: 0px;
    width: 350px;
    height: 420px;
    // background: inherit;
    background-color: rgba(255, 255, 255, 1);
    border: none;
    border-radius: 10px;
    -moz-box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    -webkit-box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    // font-family: '寰蒋闆呴粦 Bold', '寰蒋闆呴粦 Regular', '寰蒋闆呴粦';
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
    // color: #999999;
    color:black;
    text-align: left;
    line-height: 20px;
  }
  .login-form {
    position: fixed;
    left: 50%;
    margin-left: -175px;
    top: 50%;
    margin-top: -210px;
  }
  .ax_default {
    font-family: 'ArialMT', 'Arial';
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    letter-spacing: normal;
    color: #666666;
    vertical-align: none;
    text-align: center;
    line-height: normal;
    text-transform: none;
  }
  #u18_img {
    border-width: 0px;
    left: 0px;
    top: 0px;
    width: 22.858em;
    margin-top: 25px;
  }

  .login_title{
    font-family: 'PingFangSC-Regular', 'PingFang SC';
    font-weight: 400;
    font-style: normal;
    font-size: 24px;
    color: #692B80;
  }
  .lgn_row_top{
    height: 2.5em;
  }
  .lgn_row_bottom{
    margin-top:1em;
  }
  #u2_text{
    margin-top: -35px
  }
  .login_font{
    font-family: 'PingFangSC-Regular', 'PingFang SC';
    font-weight: 400;
    font-style: normal;
    font-size: 0.715em;
    color:#666666;
    margin-left:25px;
    margin-right:25px;
  }
  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;
    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }
  .svg-container {
    // padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }
  .title-container {
    position: relative;
    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }
  .show-pwd {
    position: absolute;
    right: 10px;
    top: 4px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }
  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>
