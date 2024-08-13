<template>
  <div>
    <h2>Influencers</h2>
    <table class="table table-dark">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Influencer Name</th>
          <th scope="col">category</th>
          <th scope="col">Niche</th>
          <th scope="col">Reach</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="influencer in influencers" :key="influencer.id">
          <td scope="row">{{ influencer.influencer_id }}</td>
          <td>{{ influencer.influencer_name}}</td>
          <td>{{ influencer.category }}</td>
          <td>{{ influencer.niche }}</td>
          <td>{{ influencer.reach }}</td>
          <td>

            <button @click="deleteInfluencer(influencer.influencer_id)" class="btn btn-danger"  style="font-size:12px;margin:4px"><i class="fa-solid fa-trash"></i>  Remove</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'InfluencerRequest',
  data() {
    return {
      influencers: [],
      user_id :"",
      user_name:"",
    };
  },
  methods: {
    fetchInfluencerRequests() {
      axios.get('http://127.0.0.1:5000/api/influencers', {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.influencers = response.data.data;
        this.user_id = response.data.data.user_id;
        
      })
      .catch(error => {
        console.error('Error fetching sponsor requests:', error);
      });
    },

    deleteInfluencer(influencerId) {
      axios.delete(`http://127.0.0.1:5000/api/influencer/${influencerId}`, {
        headers: {
          'Authorization': localStorage.getItem('authToken')
        }
      })
      .then(response => {
        this.fetchInfluencerRequests();
        alert('influencer deleted successfully')
      })
      .catch(error => {
        console.error('Error deleting influencer:', error);
      });
    }
  },
  created() {
    this.fetchInfluencerRequests();
  }
};
</script>