import Vue from 'vue';
import Vuex from 'vuex';
import router from './router';
import AXIOS from './common/http-common';
import UIKit from "uikit";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isAuthenticated: localStorage.getItem('authtoken') !== null,
        isRefreshing: false,
        refreshingCall: undefined,
        token: localStorage.getItem('authtoken'),
        refreshToken: localStorage.getItem('refreshToken'),
        user: {
            username: localStorage.getItem('username'),
            name: localStorage.getItem('name'),
            email: localStorage.getItem('email'),
            id: localStorage.getItem('id'),
        },
        errors: {},
        errorMessage: '',
        applicationStatuses: [],
    },
    mutations: {
        setIsAuthenticated(state, payload) {
            state.isAuthenticated = payload;
        },
        setUser(state, payload) {
            localStorage.setItem('username', payload.username);
            localStorage.setItem('name', payload.full_name);
            localStorage.setItem('email', payload.email);
            localStorage.setItem('id', payload.id);
            state.user.username = payload.username;
            state.user.name = payload.full_name;
            state.user.email = payload.email;
            state.user.id = payload.id;
        },
        setRefreshingState(state, payload) {
            state.isRefreshing = payload;
        },
        setRefreshingCall(state, payload) {
            state.refreshingCall = payload;
        },
        setApplicationStatuses(state, payload) {
            state.applicationStatuses = payload;
        },
        setToken(state, payload) {
            localStorage.setItem('authtoken', payload.access);
            localStorage.setItem('refreshToken', payload.refresh);
            state.token = payload.access;
            state.refreshToken = payload.refresh;
        },
        removeToken(state) {
            localStorage.removeItem('authtoken');
            localStorage.removeItem('refreshToken');
            localStorage.removeItem('username');
            localStorage.removeItem('name');
            localStorage.removeItem('email');
            localStorage.removeItem('id');
            state.user.username = '';
            state.user.name = '';
            state.user.email = '';
            state.user.id = '';
            state.token = '';
            state.refreshToken = '';
        },
        setErrors(state, payload) {
            if (payload.detail) {
                state.errors = {};
                state.errorMessage = payload.detail;
            } else if (payload.constructor === ({}).constructor) {
                state.errors = payload;
                state.errorMessage = '';
            } else {
                state.errors = {};
                state.errorMessage = 'مشکلی پیش آمده';
            }
            if (state.errorMessage && state.errorMessage !== '') {
                UIKit.notification(`<span uk-icon='icon: warning'></span>${state.errorMessage}`, {status: 'danger'});
            }
        },
        emptyErrors(state) {
            state.errors = {};
            state.errorMessage = '';
        }
    },
    actions: {
        async userLogin({commit, dispatch}, {username, password}) {
            try {
                const response = await AXIOS.post(`auth/token/`, {
                    username,
                    password
                });
                commit('setIsAuthenticated', true);
                commit('setToken', response.data);
                dispatch('getCurrentUser');
                router.push('/dashboard');
            } catch (e) {
                commit('setIsAuthenticated', false);
                commit('removeToken');
                commit('setErrors', e.response.data);
            }
        },
        async getCurrentUser({commit}) {
            try {
                const user = await AXIOS.get(`users/users/current-user/`);
                commit('setUser', user.data);
            } catch (e) {
                commit('setErrors', e.response.data);
            }
        },
        async getApplicationStatuses({commit}) {
            try {
                const statuses = await AXIOS.get(`jobs/applicants/statuses/`);
                commit('setApplicationStatuses', statuses.data);
            } catch (e) {
                commit('setErrors', e.response.data);
            }
        },
        userSignOut({commit}) {
            commit('setIsAuthenticated', false);
            commit('removeToken');
            router.push('/');
        },
        emptyErrors({commit}) {
            commit('emptyErrors');
        }
    }
});
