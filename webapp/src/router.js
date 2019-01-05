import Vue from 'vue';
import Router from 'vue-router';
import CarolorMap from '@/views/CarolorMap.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'carolormap',
      component: CarolorMap,
    },
  ],
});
