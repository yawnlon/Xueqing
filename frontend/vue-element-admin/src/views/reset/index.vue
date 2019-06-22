<template>
    <el-row class="container" type='flex' justify='center' align='middle'>
        <el-row class="main" type='flex' justify='center'>
            <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">
                <el-row class="r_logo" type='flex' justify='center' align='middle' style="margin:auto;margin-top:-70px;">
                    <el-col style="text-decoration:none;text-align:center;"></el-col>
                </el-row>

                <el-col type='flex' class="r_title" justify='center'>重置密码</el-col>

                
                <el-col class="r_input">
                    <el-form-item prop="username">
                        <i class="el-icon-mobile-phone"></i>
                        <el-input
                v-model="loginForm.username"
                name='username'
                placeholder="请输入账号手机号码"></el-input></el-form-item>
                </el-col>

                <el-col class="r_input"><el-form-item prop="code">
                        <i class="el-icon-message"></i>
                    <el-input
                v-model="loginForm.code"
                placeholder="请输入短信验证码"
                name='code'
                /><span class="show-pwd" style="font-size:0.8em;margin-right:0.8em" @click="reset">
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
export default {
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        // callback(new Error('Please enter the correct user name'))
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
            username: '18262610835',
            code: '111111',
        },
        loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        code: [{ required: true, trigger: 'blur', validator: validateCode,len:6 }]
      },
      message:"",
      disable:false,

    }
  },
  methods:{
      reset(){
          axios
          .post('/api/sms/send',{mobile:this.loginForm.username,template:'SMS_167655080'})
          .then(response=>(console.log(response)))
          .catch(error=>{
              this.message&&this.message.close()
              this.message=Message({
                  message:error.response.data.detail,
                  type:'error',
                  duration:3*1000,
              })
          })
      },
      nextStep(){
          this.$refs['loginForm'].validate(valid=>{
              if(valid){
                this.$router.push({ name: 'reset_input',params:{code:this.loginForm.code,mobile:this.loginForm.mobile} })
              }
          })
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
