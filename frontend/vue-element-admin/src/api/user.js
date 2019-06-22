import request from '@/utils/request'

// export function login(data) {
//   return request({
//     url: 'user/login',
//     method: 'post',
//     data
//   })
// }

export function login(data) {
  return request({
    url: '/api/v1/account/login',
    method: 'post',
    data
  })
}



export function getInfo(token) {
  return request({
    url: '/mock/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/mock/user/logout',
    method: 'post'
  })
}
