<template>
    <el-row class="container" type='flex' justify='center' align='middle'>
        <el-row class="main" type='flex' justify='center'>
            <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">
                <el-row class="r_logo" type='flex' justify='center' align='middle' style="margin:auto;margin-top:-70px;overflow:hidden">
                    <img id="u18_img" class="img" :src="log_img" style="width:9em">
                </el-row>

                <el-col type='flex' class="r_title" justify='center'>重置密码</el-col>

                
                <el-col class="r_input">
                    <el-form-item prop="mobile">
                        <i class="el-icon-mobile-phone"></i>
                        <el-input
                v-model="loginForm.mobile"
                name='mobile'
                ref='mobile'
                placeholder="请输入账号手机号码"></el-input></el-form-item>
                </el-col>

                <el-col class="r_input"><el-form-item prop="code">
                        <i class="el-icon-message"></i>
                    <el-input
                v-model="loginForm.code"
                placeholder="请输入短信验证码"
                name='code'
                /><span class="show-pwd" style="font-size:0.8em;margin-right:0.8em" @click="sendCode">
                发送验证码
            </span></el-form-item>
            </el-col>

                <el-col class="r_button"><el-button type="primary"
                :disabled="disable"
                @click="nextStep">下一步</el-button></el-col>
                <!-- <router-link :to="{ name: 'reset_input', params: { username:'asdfasd' }}"></router-link> -->
            </el-form>
        </el-row>
    </el-row>
</template>

<script>
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import { validUsername, isPhone } from '@/utils/validate'
import log_img from '@/assets/front/logo-part4.png'
export default {
  data() {
    const validateMobile = (rule, value, callback) => {
      if (!isPhone(value)) {
        this.message&&this.message.close()
        this.message=Message({
              message: '手机格式错误',
              type: 'error',
              duration: 3 * 1000
            })
        callback()
      } else {
        callback()
      }
    }
    const validateCode = (rule, value, callback) => {
      if (value.length!=6) {
        // callback(new Error('The password can not be less than 6 digits'))
        let error_msg = '验证码位数应为6位'
        this.message&&this.message.close()
        this.message = Message({
        message:error_msg,
        type:'error',
        duration: 3 * 1000
        })
      } else {
        callback()
      }
    }
    return {
        loginForm: {
            mobile: '18262610835',
            code: '111111',
        },
        loginRules: {
        mobile: [{ required: true, trigger: 'blur', validator: validateMobile }],
        code: [{ required: true, trigger: 'blur', validator: validateCode,len:6 }]
      },
      message:"",
      disable:false,
      log_img:log_img+ '?' + +new Date(),
      codeMsg : '重发验证码',
      countdown : 60,
      timer : null,
      codeDisabled : false,
    }
  },
  methods:{
      nextStep(){
          this.$refs['loginForm'].validate(valid=>{
              if(valid){
                this.$router.push({ name: 'reset_input',params:{code:this.loginForm.code,mobile:this.loginForm.mobile} })
              }
          })
      },
      sendCode() {
      // 检查手机号
      if (!this.loginForm.mobile) {
        this.$refs['loginForm'].fields[1].validateMessage = '请输入手机号'
        this.$refs['loginForm'].fields[1].validateState = 'error'
        return
      }
      // 验证码60秒倒计时
      if (!this.timer) {
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
        axios
          .post('/api/sms/send', {mobile:this.loginForm.mobile,template:'SMS_167655080'})
          .then(response => (console.log(response)))
          .catch(function(error) { // 请求失败处理
            Message({
              message: error.response.data.detail,
              type: 'error',
              duration: 3 * 1000
            })
            // console.log(error.response.data.detail)
          })
      }
    }
  },
    watch:{
        'loginForm.code':{
            deep:true,
            handler(n,o){
                if(n.length==6){
                    this.disable=false
                }else{
                    this.disable=true
                }
            }
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

.container{
    
    height: inherit;
    background-color: $bg;

    .main{
        width: 460px;
        height: 460px;
        font-family: '微软雅黑';
        font-weight: 400;
        font-style: normal;
        // text-align: left;
        line-height: 20px;
        background-color:rgba(255, 255, 255, 1);
        

        div.r_input{
            margin-left:30px;
            margin-top:20px;

            .el-input {
                display: inline-block;
                height: 47px;
                width: 85%;

                input {
                background: transparent;
                border: 0px;
                -webkit-appearance: none;
                border-radius: 0px;
                padding: 12px 5px 12px 15px;
                color: $more_gray;
                height: 47px;
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
            margin-left: 25px;
            margin-right:25px;
            padding-left:10px;
        }

        

        .r_title{
            text-align: center;
            margin:0px;
            width:100%;
            height:70px;
            font-weight: 700;
            font-style: normal;
            font-size: 20px;
            color: #999999;
            line-height: 36px;

        }

        .r_logo{
            border-width: 0px;
            width: 140px;
            height: 140px;
            display: flex;
            font-weight: 700;
            font-style: normal;
            font-size: 20px;
            color: #999999;
            line-height: 36px;
            border-radius: 284px;
            background-color:rgba(255, 255, 255, 1);
        }
        
        

    }
     div{
            display: block;
            width:350px;

    }
     div.r_button{
            width: 100%;
            text-align: center;
            
            button{
                width: 350px;
            }
    }
    .show-pwd {
        position: absolute;
        right: 10px;
        top: 7px;
        font-size: 16px;
        color: $dark_gray;
        cursor: pointer;
        user-select: none;
    }
    
    
}

</style>
