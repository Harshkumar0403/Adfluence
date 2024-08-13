<template>
  <div>
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">Ad Requests</h2>
    <div  v-if="filteredAdRequests.length === 0">No ad requests available.</div>
    <div class="all-cards">
      <div v-for="adRequest in filteredAdRequests" :key="adRequest.id" class="ad-request-card">
      <p ><strong style="color:#283618">Campaign Name:</strong> {{ campaignNames[adRequest.campaign_id]  }}</p>
      <p><strong style="color:#283618">Ad Name:</strong> {{  adNames[adRequest.ad_id]  }}</p>
      <p><strong style="color:#283618">Sponsor Name:</strong> {{ sponsorNames[adRequest.sponsor_id] }}</p>
      <p><strong style="color:#283618">Content:</strong> {{ adRequest.content }}</p>
      <p><strong style="color:#283618">Requirements:</strong> {{ adRequest.requirements }}</p>
      <p><strong style="color:#283618">Budget:</strong> {{ adRequest.budget }}</p>
      <div>
        <button @click="updateAdRequestStatus(adRequest.id, 'accepted')" style="background-color:green"><i class="fa-solid fa-check"></i> Accept</button>
        <button @click="updateAdRequestStatus(adRequest.id, 'rejected')" style="background-color:red"><i class="fa-solid fa-xmark"></i> Reject</button>
      </div>
    </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AdRequests',
  data() {
    return {
      adname:"",
      campaign_name:"",
      company_name:"",
      adRequests: [],
      campaignNames: {},
      adNames: {},
      sponsorNames: {},
      authToken: localStorage.getItem('authToken'),
      influencerId: localStorage.getItem('influencer_id'),
      sponsorId: localStorage.getItem('sponsor_id'), 
      company_name : localStorage.getItem('company_name')// Assuming the influencer_id is stored in localStorage
    };
  },
  computed: {
    filteredAdRequests() {
      return this.adRequests.filter(adRequest => {
        if (this.influencerId) {
          return adRequest.influencer_id === parseInt(this.influencerId) && adRequest.status === 'pending';
        } else if (this.sponsorId) {
          return adRequest.sponsor_id === parseInt(this.sponsorId) && adRequest.status === 'pending';
        }
        return false;
      });
    }
  },
  methods: {
    fetchAdRequests() {
      axios.get('http://127.0.0.1:5000/api/ad_request', {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.adRequests = response.data.data.map(adRequest => {
          // Assuming the API returns the necessary fields
          return {
            id: adRequest.id,
            campaign_id: adRequest.campaign_id, // You may need to fetch additional data to resolve names
            ad_id: adRequest.ad_id,
            sponsor_id: adRequest.sponsor_id,
            content: adRequest.message,
            status:adRequest.status,
            requirements: adRequest.requirements,
            budget: adRequest.payment,
            influencer_id: adRequest.influencer_id
          };
          
        });
        this.adRequests.forEach(adRequest => {
          this.fetchCampaignName(adRequest.campaign_id);
          this.fetchAdName(adRequest.ad_id);
          this.fetchSponsorName(adRequest.sponsor_id);
          console.log(this.adRequests)
        });
      })
      .catch(error => {
        console.error('Error fetching ad requests:', error);
      });
    },
    fetchAdName(adId) {
      if (!this.adNames[adId]) {
        axios.get(`http://127.0.0.1:5000/api/Ad/${adId}`, {
          headers: {
            'Authorization': this.authToken
          }
        })
        .then(response => {
          this.adNames = { ...this.adNames, [adId]: response.data.data.name };
        })
        .catch(error => {
          console.error('Error fetching ad name:', error);
        });
      }
    },
     fetchSponsorName(sponsorId) {
      if (!this.sponsorNames[sponsorId]) {
        axios.get(`http://127.0.0.1:5000/api/sponsor/${sponsorId}`, {
          headers: {
            'Authorization': this.authToken
          }
        })
        .then(response => {
          this.sponsorNames = { ...this.sponsorNames, [sponsorId]: response.data.data.company_name };
        })
        .catch(error => {
          console.error('Error fetching sponsor name:', error);
        });
      }
    },
    fetchCampaignName(campaignId) {
      if (!this.campaignNames[campaignId]) {
        axios.get(`http://127.0.0.1:5000/api/campaign/${campaignId}`, {
          headers: {
            'Authorization': this.authToken
          }
        })
        .then(response => {
          this.campaignNames = { ...this.campaignNames, [campaignId]: response.data.data.name };
        })
        .catch(error => {
          console.error('Error fetching campaign name:', error);
        });
      }
    },
    fetchSponsor(id){
      const authToken = localStorage.getItem('authToken');
      axios.get(`http://127.0.0.1:5000/api/sponsor/${id}`, {
        headers: {
          'Authorization': authToken,
        },
      })
      .then(response => {
        this.company_name = response.data.data.company_name;
      })
      .catch(error => {
        console.error('An error occurred while fetching the campaigns:', error);
      });

    },
    updateAdRequestStatus(adRequestId, status) {
     axios.put(`http://127.0.0.1:5000/api/ad_request/${adRequestId}`, { status }, {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        alert(`Ad request ${status} successfully`);
        this.fetchAdRequests(); // Refresh the ad requests list
      })
      .catch(error => {
        console.error(`Error updating ad request status to ${status}:`, error);
      });
    }
  },
  created() {
    this.fetchAdRequests();
  }
};
</script>

<style scoped>
.all-cards{
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.ad-request-card {
  border: 1px solid #ccc;
  padding: 20px;
  background-color: #9f7e69;
  color: #e3d5ca;
  margin-bottom: 10px;
  border-radius: 10px;

  width: calc(33.333% - 20px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
button {
  margin: 8px;
  border-radius:10px;
  color:#ddd;
  border:none;
  background-color: darkolivegreen;
  font-size: 20px;
  align-content: center;
  cursor: pointer;
}
button:hover {
  background-color: #99582a;
}
</style>