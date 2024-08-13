<template>
  <div class="influencers-container">
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;"> All Influencers</h2>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-else class="influencer-cards">
      <div class="influencer-card" v-for="influencer in influencers" :key="influencer.id">
        <div class="influencer-content">
          <h3 style="background-color:#219ebc"><strong>{{ influencer.influencer_name}}</strong></h3>
          <div style="background-color:#52b69a"></div>
          <p><strong>Category:</strong> {{ influencer.category }}</p>
          <p><strong>Reach:</strong> {{ formatReach(influencer.reach) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Influencers',
  data() {
    return {
      influencers: [],
      error: null,
    };
  },
  created() {
    this.fetchInfluencers();
  },
  methods: {
    fetchInfluencers() {
      const authToken = localStorage.getItem('authToken');
      axios.get('http://127.0.0.1:5000/api/influencers', {
        headers: {
          'Authorization': `Bearer ${authToken}`,
        },
      })
      .then(response => {
        console.log(response.data.data); // Check the structure of the response
        this.influencers = response.data.data;
      })
      .catch(error => {
        console.error('An error occurred while fetching the influencers:', error);
        this.error = 'An error occurred while fetching the influencers. Please try again.';
      });
    },
    formatReach(reach) {
      if (reach >= 1000000) {
        return (reach / 1000000).toFixed(1) + 'M';
      }
      if (reach >= 1000) {
        return (reach / 1000).toFixed(1) + 'K';
      }
      return reach;
    },
  },
};
</script>

<style scoped>
.influencers-container {
  padding: 20px;
}
.error {
  color: red;
}
.influencer-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.influencer-card {
  background-color: #faedcd;
  border: 1px solid #ddd;
  border-radius: 8px;
  width: calc(33.333% - 20px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 15px;
  height: 130px;
}
.influencer-content {
  padding: 7px;
  font-size: 12px;
}
</style>
