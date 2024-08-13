<template>
  <div class="campaigns-container">
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">All Campaigns</h2>
    <div class="campaign-cards">
      <div class="campaign-card" v-for="campaign in campaigns" :key="campaign.id">
        <img :src="getImagePath(campaign.campaign_img)" alt="Campaign Image" class="campaign-image">
        <div class="campaign-content">
          <p style="font-size:15px;background-color:#219ebc;text-align:center;font-style: italic"><h3  style="background-color:#219ebc"><strong>{{campaign.name}}</strong></h3>{{campaign.description}}</p>
          <div class="campaign-details" style="background-color:#d8e2dc;font-size:10px">
            <p><strong>Budget:</strong> {{ formatBudget(campaign.budget) }}</p>
            <p><strong>Goals:</strong> {{campaign.goals}}</p>
            <p><strong>Ends at: </strong>{{ formatDate(campaign.end_date) }}</p>
            <button v-if="this.role === 'sponsor'" @click="editCampaign(campaign.id)"><i class="fa-regular fa-pen-to-square"></i> Edit</button>
            <button v-if="this.role === 'sponsor'" @click="deleteCampaign(campaign.id)"><i class="fa-solid fa-trash"></i> Delete</button>
            <button v-if="this.role === 'sponsor'" @click="addAd(campaign.id)"><i class="fa-solid fa-plus"></i> Ad</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Campaigns',
  props: {
    campaign: Object,
  },
  data() {
    return {
      campaigns: [],
      role : localStorage.getItem('role')
    };
  },
  created() {
    this.fetchCampaigns();
  },
  computed: {
    formattedEndDate() {
      return this.formatDate(this.campaign.end_date);
    },
    formattedBudget() {
      return this.formatBudget(this.campaign.budget);
    },
  },
  methods: {
    fetchCampaigns() {
      const authToken = localStorage.getItem('authToken');
      axios.get('http://127.0.0.1:5000/api/campaign', {
        headers: {
          'Authorization': authToken,
        },
      })
      .then(response => {
        console.log(response.data.data[0].status)
        for(let i=0;i<response.data.data.length;i++){
          if(response.data.data[i].status==='approved'){
            this.campaigns[i]=response.data.data[i]
          }
        }
      })
      .catch(error => {
        console.error('An error occurred while fetching the campaigns:', error);
      });
    },
     getImagePath(filename) {
      return require(`../../../frontend/src/assets/campimg/${filename}`);
    },
    formatBudget(budget) {
      return `${(budget / 1000).toFixed(1)}k`;
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      const options = { year: 'numeric', month: 'long', day: '2-digit' };
      return date.toLocaleDateString(undefined, options);
    },
     deleteCampaign(id) {
      axios.delete(`http://127.0.0.1:5000/api/campaign/${id}`)
        .then(response => {
          alert('Campaign deleted successfully');
          // Add logic to update UI after deletion
          this.fetchCampaigns();
          this.$emit('campaignDeleted', this.campaign.id);
        })
        .catch(error => {
          console.error('Error deleting campaign:', error);
          alert('Failed to delete campaign');
        });
    },
     editCampaign(id) {
      this.$router.push({ name: 'EditCampaign', params: { id: id } });
    },
    addAd(id) {
      this.$router.push({ name: 'AddAd', params: { id: id } });
    },
  },
};
</script>

<style scoped>
.campaigns-container {
  padding: 20px;
}
.campaign-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.campaign-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  width: calc(33.333% - 20px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.campaign-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.campaign-content {
  padding: 7px;
}
.campaign-details {
  margin-top: 10px;
  padding: 7px;
}
button {
  margin: 8px;
  border-radius:10px;
  color:#ddd;
  border:none;
  background-color: darkolivegreen;
  font-size: 12px;
  align-content: center;
  cursor: pointer;
  
}
button:hover {
  background-color: #99582a;
}
</style>
