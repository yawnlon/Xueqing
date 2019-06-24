<template>
  <el-row class="container" :style="bg_img" type="flex" justify="center" align="middle">
    <el-row class="main" type="flex" justify="center">
      <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="off" label-position="left">
        <el-col class="r_title"><img id="u18_img" class="img" :src="log_img" style="width:16em;margin-top:25px;"></el-col>
        <el-col class="r_button"><el-button type="primary" class="reset-button">重置密码</el-button></el-col>

        <el-col class="r_input">
          <el-form-item prop="pwd">
            <svg-icon icon-class="password" />
            <el-input
              ref="pwd"
              v-model="loginForm.pwd"
              type="password"
              placeholder="设置6至20位登录密码"
            /></el-form-item>
        </el-col>

        <el-col class="r_input">

          <el-form-item prop="newpwd">
          <svg-icon icon-class="password" />
          <el-input
            ref="newpwd"
            v-model="loginForm.newpwd"
            type="password"
            placeholder="请再次输入登录密码"
          >
            <!-- <span class="show-pwd" style="font-size:0.8em" @click="function(){}">
                发送验证码
            </span> -->
          </el-input>
        </el-form-item>

        </el-col>
           
        <el-col class="r_button"><el-button type="primary" :disabled="disable" @click="checkpwd">下一步</el-button></el-col>
      </el-form>
    </el-row>
    <Footer/>
  </el-row>
</template>

<script>
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import { validUsername, isPhone } from '@/utils/validate'
import log_img from '@/assets/front/logo-part3.png'
export default {
  components: { Footer:require('@/views/common/footer').default},
  data() {
    const validatePassword = (rule, value, callback) => {
      if(this.loginForm.pwd===this.loginForm.newpwd){
        callback()
      }else{
        callback('两次密码不一致')
      }
    }
   
    return {
      loginForm: {
        pwd: '',
        newpwd: ''
      },
      loginRules: {
        pwd: [{ required: true, trigger: 'blur', message:'请输入密码'},{ trigger: 'blur', min:6,max:20,message:'密码为6-20位字符'}],
        newpwd: [{ required: true, trigger: 'blur', message:'请再次输入密码'},{trigger:'mouseout',min:6,max:20, validator: validatePassword }],
      },
      message: '',
      log_img: log_img,
      bg_img: 'background-image:url(' + require('@/assets/front/bg-01.png') + ');background-repeat: no-repeat;background-size:100% 100%;-moz-background-size:100% 100%;',
      disable: true,
    }
  },
  watch: {
    'loginForm.newpwd': {
      deep: true,
      handler(n, o) {
        if (this.loginForm.newpwd === this.loginForm.pwd && this.loginForm.newpwd.length >= 6) {
          this.disable = false
        } else if(this.loginForm.newpwd.length>=6) {
          this.disable = true
          this.$refs.loginForm.validateField('newpwd');
        }
      }
    }
  },
  created() {
    // Object.keys(a).length
    if (Object.keys(this.$route.params).length == 0) {
      this.$router.push({ path: '/' })
    }
  },
  methods: {
    
    checkpwd() {
      this.$refs['loginForm'].validate(valid => {
        if (!valid) {
          const error_msg = this.loginForm.pwd === this.loginForm.newpwd ? false : '两次输入密码不一致'
          this.message && this.message.close()
          this.message = Message({
            message: error_msg,
            type: 'error',
            duration: 5 * 1000
          })
          this.$refs.newpwd.focus()
          return false
        } else {
          axios
            .post('/api/v1/account/reset-password', { mobile: this.$route.params.mobile, code: this.$route.params.code, password: this.loginForm.newpwd, pwdcp: this.loginForm.pwd })
            .then(
              (response) => {
                console.log(response)
                this.$router.push({ path: '/success', query: { tip: '密码重置成功', redirect: '/login', content: '重新登录' }})
              })
            .catch(error => {
              console.log(error.response)
            })
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
    .el-form-item__error{
      margin-bottom:2px;
    }
  
}
.el-button--primary{
    background-color: rgba(2, 167, 240, 1);
}


</style>
