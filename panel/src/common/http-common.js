import axios from 'axios';
import store from '../store';

const AXIOS = axios.create({
    baseURL: process.env.VUE_APP_API_ROOT,
});

AXIOS.interceptors.request.use(
    config => {
        if (store.state.isAuthenticated) {
            config.headers.Authorization = `Bearer ${store.state.token}`;
        }
        return config;
    },
    error => Promise.reject(error)
);

AXIOS.interceptors.response.use(
    response => response,
    error => {
        const status = error.response ? error.response.status : null;
        if (store.state.isAuthenticated && status === 401 && error.response.config.url !== 'auth/refresh/') {
            return refreshToken(store)
                .then(() => {
                    console.log('success');
                    error.config.headers['Authorization'] = 'Bearer ' + store.state.token;
                    error.config.baseURL = undefined;
                    return AXIOS.request(error.config);
                })
                .catch(e => {
                    store.dispatch('userSignOut');
                    return Promise.reject(e);
                });
        }
        return Promise.reject(error);
    }
);

function refreshToken(store) {
    if (store.state.isRefreshing) {
        return store.state.refreshingCall;
    }
    store.commit('setRefreshingState', true);
    const refreshingCall = AXIOS.post('auth/refresh/', {
        refresh: store.state.refreshToken
    }).then(({data: {access}}) => {
            store.commit('setToken', {accessToken: access, refreshToken: store.state.refreshToken});
            store.commit('setRefreshingState', false);
            store.commit('setRefreshingCall', undefined);
            return Promise.resolve(true);
        }).catch(e => {
            return Promise.reject(e);
        });
    store.commit('setRefreshingCall', refreshingCall);
    return refreshingCall;
}

export default AXIOS;
