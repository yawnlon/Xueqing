<template>
    <el-row class="container" type='flex' justify='center' align='middle'>
        <el-row class="main" type='flex' justify='center'>

            <el-row class="r_logo" type='flex' justify='center' align='middle' style="margin:auto;margin-top:-70px;">
                <el-col style="text-decoration:none;text-align:center;">LOGO</el-col>
            </el-row>

            <el-col type='flex' class="r_title" justify='center'>重置密码</el-col>


            <el-col class="r_input"><el-input
            prefix-icon='el-icon-mobile-phone'
            v-model="input"
            placeholder="请输入账号手机号码"></el-input></el-col>
            

            <el-col class="r_input"><el-input
            prefix-icon='el-icon-message'
            v-model="input"
            placeholder="请输入短信验证码"><span class="show-pwd" style="font-size:0.8em" @click="function(){}">
            发送验证码
          </span></el-input></el-col>
            <el-col class="r_button"><el-button type="primary">主要按钮</el-button></el-col>
        </el-row>
    </el-row>
</template>

<script>
export default {
  data() {
    return {
      input: ''
    }
  }
}

</script>

<style lang="scss" scoped>

$bg:rgba(240, 242, 245, 1);
$dark_gray:#889aa4;


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
            margin-left:55px;
            margin-top:20px;
            
            &input{
                height:50px;
            }
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
    & div{
            display: block;
            width:350px;

    }
    & div.r_button{
            width: 100%;
            text-align: center;
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
