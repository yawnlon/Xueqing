<template>
    <el-row class="container" type='flex' justify='center' align='middle'>
        <el-row class="main" type='flex' justify='center'>
            <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">
                <el-row class="r_logo" type='flex' justify='center' align='middle' style="margin:auto;margin-top:-70px;overflow:hidden">
                    <img id="u18_img" class="img" :src="log_img" style="width:9em">
                </el-row>

                <el-col type='flex' class="r_title" justify='center'>重置密码</el-col>

                <el-col class="r_input">
                    <el-form-item prop="pwd">
                        <i class="el-icon-mobile-phone"></i>
                        <el-input
                v-model="loginForm.pwd"
                name='pwd'
                ref = 'pwd'
                type='password'
                placeholder="设置6至20位登录密码"></el-input></el-form-item>
                </el-col>
                
                <el-col class="r_input"><el-form-item prop="newpwd">
                        <i class="el-icon-message"></i>
                    <el-input
                v-model="loginForm.newpwd"
                name = 'newpwd'
                ref='newpwd'
                type='password'
                placeholder="请再次输入登录密码"><span class="show-pwd" style="font-size:0.8em" @click="function(){}">
                发送验证码
            </span></el-input></el-form-item>
            </el-col>

                <el-col class="r_button"><el-button type="primary" @click="checkpwd">下一步</el-button></el-col>
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
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6&&value.length>0) {
        // callback(new Error('The password can not be less than 6 digits'))
        let error_msg = '密码不能低于6位'
        this.message && this.message.close()
        this.message = Message({
          message:error_msg,
          type:'error',
          duration: 5 * 1000
        })
      } else {
        callback()
      }
    }
    return {
        loginForm: {
            pwd: '',
            newpwd: '',

        },
        loginRules: {
          pwd: [{ required: true, trigger: 'blur', validator: validatePassword }],
          newpwd: [{ required: true, trigger: 'blur', validator: validatePassword }]
        },
        message:'',
        log_img:log_img+ '?' + +new Date(),

    }
  },
  methods:{
    checkpwd(){
      this.$refs['loginForm'].validate(valid=>{
        if(!valid){
             let error_msg = this.loginForm.pwd===this.loginForm.newpwd ? false:'两次输入密码不一致'
            this.message&&this.message.close()
            this.message=Message({
              message:error_msg,
              type:'error',
              duration: 5 * 1000
            })
            this.$refs.newpwd.focus()
            return false
        }else{
          axios
          .post('/api/account/reset-password',{mobile:this.$route.params.mobile,code:this.$route.params.code,password:this.loginForm.newpwd,pwdcp:this.loginForm.pwd})
          .then(response=>console.log(response))
          .catch(error=>{
            console.log(error.response)
          })
          this.$router.push({path:'/success'})
        }

      })
     
      
    }
  },
  watch:{
    
    
  },

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
