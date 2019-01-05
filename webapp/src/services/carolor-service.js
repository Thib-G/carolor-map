import axios from 'axios';

export default {
  getAllPartners() {
    return axios.get('/api/partners/all').then(response => response.data);
  },
};
