<template>
  <el-row class="container" :style="bg_img" type="flex" justify="center" align="middle">
    <el-row class="main" type="flex" justify="center">
      <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">

        <el-col class="r_title"><img id="u18_img" class="img" :src="log_img" style="width:16em;margin-top:25px;"></el-col>
        <el-col class="r_button"><el-button type="primary" class="reset-button">重置密码</el-button></el-col>
        <el-col class="r_input">
          <el-form-item prop="mobile">
            <svg-icon icon-class="mobile" />
            <el-input
              ref="mobile"
              v-model="loginForm.mobile"
              name="mobile"
              placeholder="请输入账号手机号码"
            /></el-form-item>
        </el-col>

        <el-col class="r_input"><el-form-item prop="code">
         <svg-icon icon-class="email" />
          <el-input
            ref="cdoe"
            v-model="loginForm.code"
            placeholder="请输入短信验证码"
            name="code"
          />
          <!-- <span class="show-pwd" style="font-size:0.8em;margin-right:0.8em" @click="sendCode">
                发送验证码
            </span> -->
          <el-button type="text" class="show-pwd" style="font-size:0.8em;color:#02A7F0" :disabled="codeDisabled" @click.native.prevent="sendCode()">
            {{ codeMsg }}
          </el-button>
        </el-form-item>
        </el-col>

        <el-col class="r_button"><el-button
          type="primary"
          :disabled="disable"
          @click="nextStep"
        >下一步</el-button></el-col>
        <!-- <router-link :to="{ name: 'reset_input', params: { username:'asdfasd' }}"></router-link> -->
      </el-form>
    </el-row>
    <Footer/>
  </el-row>
</template>

<script>
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
// import { validUsername, isPhone } from '@/utils/validate'
import log_img from '@/assets/front/logo-part3.png'
export default {
  components: { Footer:require('@/views/common/footer').default},
  data() {
    return {
      loginForm: {
        mobile: '',
        code: ''
      },
      loginRules: {
        mobile: [
          { required: true, trigger: 'blur', message: '请输入手机号码' },
          { pattern: /^((1[3,5,8][0-9])|(14[5,7])|(17[0,5,6,7,8])|(19[7]))\d{8}$/, message: '请检查手机号是否正确', trigger: 'blur' }
        ],
        code: [
          { required: true, trigger: 'blur', message: '请输入短信验证码' },
          { len: 6, message: '短信验证码为6位数字', trigger: 'blur' }
        ]
      },
      message: '',
      disable: true,
      log_img: log_img, // + '?' + +new Date(),
      codeMsg: '重发验证码',
      countdown: 60,
      timer: null,
      bgImg: 'background-image:url(' + require('@/assets/front/bg-01.png') + ');background-repeat: repeat;background-color: #02a7f0;',
      log_img: log_img, // + '?' + +new Date(),
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
    'loginForm.code': {
      deep: true,
      handler(n, o) {
        // this.source = this.axios.CancelToken.source(); // 这里初始化source对象
        if (n.length == 6) {
          axios
            .post('/api/v1/sms/verify', { mobile: this.loginForm.mobile, code: this.loginForm.code })
            .then(response => {
              this.disable = false
            })
            .catch(error => {
              this.disable = true
            })
        }
      }
    }

  },
  mounted() {
    // if (this.loginForm.mobile === '') {
    //   this.$refs.mobile.focus()
    // } else if (this.loginForm.code === '') {
    //   this.$refs.code.focus()
    // }
  },
  methods: {
    nextStep() {
      this.$refs['loginForm'].validate(valid => {
        if (valid) {
          this.$router.push({ name: 'reset_input', params: { code: this.loginForm.code, mobile: this.loginForm.mobile }})
        }
      })
    },
    sendCode() {
      const self = this
      this.$refs.loginForm.validateField('mobile', (error) => {
        if (!error) {
          // 验证码60秒倒计时
          if (!this.timer) {
            axios
              .post('/api/v1/sms/send', { mobile: this.loginForm.mobile, template: 'SMS_167655080' })
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
              .catch(function(error) { // 请求失败处理
                self.message && self.message.close()
                self.message = Message({
                  message: error.response.data.detail,
                  type: 'error',
                  duration: 5 * 1000
                })
                // console.log(error.response.data.detail)
              })
          }
        }
      })
    }
  }
}
</script>

<style lang="scss">
$bg:rgba(240, 242, 245, 1);
$dark_gray:#889aa4;
$mycursor:#666;
$more_gray:#999999;
$cursor: #fff;

svg{
  font-size: 18px;
}
.container{

    height: inherit;
    background-color: $bg;
    .main{
        width: 350px;
        height: 420px;
        font-family: '微软雅黑';
        font-weight: 400;
        font-style: normal;
        // text-align: left;
        line-height: 20px;
        background-color:transparent;

        div.r_input{
            // margin-left:30px;
            // margin-top:20px;
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
                    box-shadow: 0 0 0px 1000px $bg inset !important;
                    -webkit-text-fill-color: $cursor !important;
                }
                }
            }
        }

        .el-form-item {
            border: 1px solid #e2e2e2;
            background: #ffffff;
            border-radius: 5px;
            color: #454545;
            height: 42px;
            margin-left: 25px;
            margin-right:25px;
            padding-left:10px;
        }
        .el-form-item:focus-within {
          border:1px solid rgba(2, 167, 240, 1);
        }
        .r_title{
            text-align: center;
            margin:0px;
            width:100%;
            // height:70px;
            font-weight: 700;
            font-style: normal;
            font-size: 20px;
            color: #999999;
            line-height: 36px;
        }
        .r_logo{
            border-width: 0px;
            display: flex;
            font-weight: 700;
            font-style: normal;
            font-size: 20px;
            color: #999999;
            line-height: 36px;
            background-color:rgba(255, 255, 255, 1);
        }

    }

     div.r_button{
            text-align: center;
            margin-bottom: 1em;
            button{
                width: 300px;
                height: 36px;
            }
            .reset-button{
              background-color: rgba(2, 167, 240, 1);
            }
            
    }
    

    .show-pwd {
        position: absolute;
        right: 10px;
        top: 3px;
        font-size: 16px;
        color: $dark_gray;
        cursor: pointer;
        user-select: none;
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

}
.el-button--primary{
    background-color: rgba(2, 167, 240, 1);
}
</style>
