
const tokens = {
  admin: {
    token: 'admin-token'
  },
  editor: {
    token: 'editor-token'
  }
}

const users = {
  'admin-token': {
    roles: ['admin'],
    introduction: 'I am a super administrator',
    avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    name: 'Super Admin'
  },
  'editor-token': {
    roles: ['editor'],
    introduction: 'I am an editor',
    avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    name: 'Normal Editor'
  }
}

export default [
  // user login
  {
    url: '/user/login',
    type: 'post',
    response: config => {
      const { username } = config.body
      const token = tokens[username]

      // mock error
      if (!token) {
        return {
          code: 60204,
          message: 'Account and password are incorrect.'
        }
      }

      return {
        code: 20000,
        data: token
      }
    }
  },

  // get user info
  {
    url: '/user/info\.*',
    type: 'get',
    response: config => {
      const { token } = config.query
      const info = users[token]
      // mock error
      if (!info) {
        return {
          code: 50008,
          message: 'Login failed, unable to get user details.'
        }
      }

      return {
        code: 20000,
        data: info
      }
    }
  },

  // user logout
  {
    url: '/user/logout',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  },

  // {
  //   url: '/account/register',
  //   type: 'post',
  //   response: _ => {
  //     return {
  //       "detail":"注册成功",
  //       "data":{
  //           "user":{
  //               "id":10,// user id
  //               "username":"xq_18813042473",
  //               "mobile":"18813042473",
  //               "type":"student",// 用户类型(分为4种，(0, 'student'), 学生用户// (1, 'admin'), 管理员// (2, 'school'), 学校用户// (3, 'agent')) 代理商
  //               "is_active":true// 是否活跃，false为已冻结
  //           },
  //           "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMCwidXNlcm5hbWUiOiJ4cV8xODgxMzA0MjQ3MyIsImV4cCI6MTU2MDY5MDAzMywiZW1haWwiOiIifQ.c_pXZ_XvSuvqy65Xb1WtdXc_ropZcpldpYiQWSXV5NM"
  //       }
  //     }
  //   }
  // }
]
