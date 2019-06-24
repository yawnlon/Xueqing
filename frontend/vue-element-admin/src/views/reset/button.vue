<template>
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">
                <el-row class="r_logo" type='flex' justify='center' align='middle' style="margin:auto;margin-top:-70px;">
                    <el-col style="text-decoration:none;text-align:center;">LOGO</el-col>
                </el-row>

                <el-col type='flex' class="r_title" justify='center'>重置密码</el-col>

                
                <el-col class="r_input">
                    <el-form-item prop="username">
                        <span class="svg-container">
                            <svg-icon icon-class="el-icon-mobile-phone" />
                        </span>
                        <el-input
                v-model="input"
                placeholder="请输入账号手机号码"></el-input></el-form-item>
                </el-col>
                

                
                <el-col class="r_input"><el-form-item prop="username">
                    <span class="svg-container">
                            <svg-icon icon-class="el-icon-mobile-phone" />
                        </span>
                    <el-input
                v-model="input"
                placeholder="请输入短信验证码"><span class="show-pwd" style="font-size:0.8em;" @click="function(){}">
                发送验证码
            </span></el-input></el-form-item>
            </el-col>

                
                <el-col class="r_button"><el-button type="primary">下一步</el-button></el-col>
            </el-form>
</template>

<script>
export default {
    name:'myButton',
    data(){
    }
}
</script>

<style lang='scss'>
$bg:rgba(240, 242, 245, 1);
$dark_gray:#889aa4;
$mycursor:#666;
$more_gray:#999999;
$cursor: #fff;
    .el-input {
        display: inline-block;
        height: 42px;
        width: 85%;
        input {
        background: transparent;
        border: 0px;
        -webkit-appearance: none;
        border-radius: 0px;
        padding: 12px 5px 12px 15px;
        color: $more_gray;
        height: 42px;
        caret-color: $mycursor;
        &:-webkit-autofill {
            box-shadow: 0 0 0px 1000px $bg inset !important;
            -webkit-text-fill-color: $cursor !important;
        }
        }
    }
    .el-form-item {
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        height: 42px;
        color: #454545;
        margin-left: 25px;
        margin-right:25px;
    }
</style>