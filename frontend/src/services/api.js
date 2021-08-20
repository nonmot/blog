import axios from 'axios'

const api = axios.create({
    baseURL: process.env.VUE_APP_ROOT_API,
    timeout: 5000,
    headers: {
        'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }
})

api.interceptors.request.use(function(config) {
    const token = localStorage.getItem('access')
    if(token) {
        config.headers.Authorization = 'JWT ' + token
        return config
    }
    return config
}, function(error) {
    return Promise.reject(error)
})

export default api