<template>
  <div>
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">All Advertisments</h2>
    <div>
      <button v-for="campaign in campaigns" :key="campaign.id" @click="showAds(campaign.id)" class="btn btn-primary">
        {{ campaign.name }}
      </button>
    </div>
    <div v-if="ads.length" class="ad-container">
      <div v-for="ad in ads" :key="ad.id" class="ad-card" >
        <h2 style="background-color:#219ebc">{{ ad.name }}</h2>
        <p><strong>Campaign: </strong>{{ ad.campaignName }}</p>
        <p><strong>Sponsor: </strong>{{ ad.sponsorCompanyName }}</p>
        <p><strong>Content: </strong> {{ ad.content }}</p>
        <p><strong>Requirements:</strong> {{ ad.requirements }}</p>
        <p><strong>Budget: </strong>{{ formatBudget(ad.budget) }}</p>
        <p><strong>Target Audience: </strong>{{ ad.target_audience }}</p>
        <p><strong>Start Date: </strong>{{ formatDate(ad.start_date) }}</p>
        <button v-if="this.role === 'sponsor'" @click="editAd(ad.id)"><i class="fa-regular fa-pen-to-square"></i> Edit</button>
        <button  v-if="this.role === 'sponsor'" @click="deleteAd(ad.id)"><i class="fa-solid fa-trash"></i> Delete</button>
           <div v-if="this.role === 'sponsor'">
            send Ad Request to Influencer
      <select v-model="selectedInfluencer[ad.id]" @change="selectInfluencer(ad.id, $event)">
        <option v-for="influencer in influencers" :key="influencer.influencer_id" :value="influencer.influencer_id">
          {{ influencer.influencer_name }}
        </option>
      </select>
      <button @click="sendAdRequest(ad.id)"><i class="fas fa-paper-plane"></i></button>
  
    </div>
    <div v-if="this.role === 'influencer'">
      send Ad Request to Sponsor
      <select v-model="selectedSponsor[ad.id]" @change="selectSponsor(ad.id, $event)">
        <option v-for="sponsor in sponsors" :key="sponsor.sponsor_id" :value="sponsor.sponsor_id">
          {{ sponsor.sponsor_name }}
        </option>
      </select>
      <button @click="sendAdRequest(ad.id)"><i class="fas fa-paper-plane"></i></button>
    </div>
        
      </div>
    </div>
  </div>
</template>
  

<script>
import axios from 'axios';

export default {
  name: 'AdComponent',
  data() {
    return {
      role:localStorage.getItem('role'),
      ads: [],
      campaigns: [],
      influencer_id:null,
      sponsor_id:null,
      users: [],
      selectedCampaignAds: [],
      selectedInfluencer: {},
      selectedSponsor: {},
      currentUserId: localStorage.getItem('sponsor_id') || localStorage.getItem('influencer_id')
    };
  },
  created() {
    this.fetchCampaigns();
    this.fetchusers();
  },
  methods: {
  async fetchAds(campaignId = null) {
    const token = localStorage.getItem('authToken');
    let url = 'http://127.0.0.1:5000/api/Ad';
    if (campaignId) {
      url += `?campaign_id=${campaignId}`;
    }
    try {
      const response = await axios.get(url, {
        headers: {
          'Authorization': token
        }
      });
      this.ads = response.data.data;
      // console.log(this.ads)
      await this.populateAdditionalInfo();
      this.selectedCampaignAds = response.data.data;
        this.selectedCampaignAds.forEach(ad => {
          if (!this.selecteduser[ad.id]) {
            this.selecteduser[ad.id] = null;
          }
        });
    } catch (error) {
      console.error('Error fetching ads:', error);
      if (error.response) {
        console.error('Server responded with status code:', error.response.status);
      }
    }
  },
   fetchInfluencers() {
      axios.get('http://127.0.0.1:5000/api/influencers', {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.influencers = response.data.data;
      })
      .catch(error => {
        console.error('Error fetching influencers:', error);
      });
    },
    fetchSponsors() {
      axios.get('http://127.0.0.1:5000/api/sponsors', {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.sponsors = response.data.data;
      })
      .catch(error => {
        console.error('Error fetching sponsors:', error);
      });
    },
  async fetchCampaigns() {
    const token = localStorage.getItem('authToken');
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/campaign', {
        headers: {
          'Authorization': token
        }
      });
      this.campaigns = response.data.data;
    } catch (error) {
      console.error('Error fetching campaigns:', error);
    }
  },
  async fetchusers() {
    const token = localStorage.getItem('authToken');
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/users', {
        headers: {
          'Authorization':token
        }
      });
      this.users = response.data.data;
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  },
  async populateAdditionalInfo() {
    const token = localStorage.getItem('authToken');
    for (const ad of this.ads) {
      try {
        const campaignResponse = await axios.get(`http://127.0.0.1:5000/api/campaign/${ad.campaign_id}`, {
          headers: {
            'Authorization':token
          }
        });
        ad.campaignName = campaignResponse.data.data.name;
        const sponsorResponse = await axios.get(`http://127.0.0.1:5000/api/sponsor/${ad.sponsor_id}`, {
          headers: {
            'Authorization': token
          }
        });
        // console.log( sponsorResponse.data.data.company_name)
        ad.sponsorCompanyName = sponsorResponse.data.data.company_name;
      } catch (error) {
        console.error('Error fetching additional info:', error);
      }
    }
  },
  formatDate(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-GB', {
      day: '2-digit',
      month: 'long',
      year: 'numeric'
    });
  },
  formatBudget(budget) {
    return budget >= 1000 ? `${(budget / 1000).toFixed(1)}k` : budget;
  },
  async deleteAd(id) {
    const token = localStorage.getItem('authToken');
    try {
      await axios.delete(`http://127.0.0.1:5000/api/Ad/${id}`, {
        headers: {
          'Authorization': token
        }
      });
      alert('Ad deleted successfully');
      this.fetchAds(this.selectedCampaignId);
    } catch (error) {
      console.error('Error deleting ad:', error);
    }
  },
  editAd(id) {
    this.$router.push({ name: 'EditAd', params: { id } });
  },
  // selectInfluencer(adId, influencerId) {
  //     // Store the selected influencer for the ad
  //       this.$set(this.selectedInfluencer, adId, influencerId);
  // },
   selectInfluencer(adId, event) {
      this.selectedInfluencer[adId] = event.target.value;
      console.log(`Selected influencer for ad ${adId}: ${this.selectedInfluencer[adId]}`);
    },
    selectSponsor(adId, event) {
      this.selectedSponsor[adId] = event.target.value;
      console.log(`Selected sponsor for ad ${adId}: ${this.selectedSponsor[adId]}`);
    },
  sendAdRequest(id) {
    const token = localStorage.getItem('authToken');
    const ad = this.selectedCampaignAds.find(ad => ad.id === id);
       if (!this.selectedInfluencer && !this.selectedSponsor) {
        alert('select member');
        return;
      }
      const isSponsor = localStorage.getItem('role') === 'sponsor';
      const adRequestData = {
        ad_id: ad.id,
        sponsor_id: isSponsor ? localStorage.getItem('sponsor_id') : this.selectedSponsor[ad.id],
        influencer_id: isSponsor ? this.selectedInfluencer[ad.id] : localStorage.getItem('influencer_id'),
        campaign_id: ad.campaign_id,
        message: `${ad.content}\n${ad.requirements}\n${ad.target_audience}\n${ad.budget}`,
        requirements: ad.requirements,
        payment: ad.budget
      };

      axios.post('http://127.0.0.1:5000/api/ad_request', adRequestData, {
        headers: {
          'Authorization': token
        }
      })
      .then(response => {
        alert('Ad request sent successfully!');
      })
      .catch(error => {
        console.error('Error sending ad request:', error);
      });
    // Logic to send ad request
  },
  showAds(campaignId) {
    this.selectedCampaignId = campaignId;
    this.fetchAds(this.selectedCampaignId);
  }
},
mounted() {
  this.fetchCampaigns();
  this.fetchInfluencers();
  this.fetchSponsors();
}
}
</script>

<style scoped>
.ad-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  
}

.ad-card {
  background-color: #faedcd;
  border: 1px solid #ccc;
  padding: 1rem;
  flex:calc(33.333% - 20px);
  /* box-sizing: border-box; */
  border-radius:10px;
  width: calc(33.3% - 15px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.campaign-buttons {
  margin-bottom: 20px;
  font-size: 12px;
}
.campaign-buttons button {
  margin-right: 10px;
}
.ad-cards {
  display: flex;
  flex-wrap: wrap;
}
.ad-card {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  width: calc(33.3% - 15px);
  box-sizing: border-box;
  font-size: 12px;
}
button {
  margin: 8px;
  border-radius:5px;
  color:#ddd;
  border:none;
  background-color: blue;
  font-size: 12px;
  cursor: pointer;
  
}
button:hover {
  background-color: #99582a;
}
</style>
