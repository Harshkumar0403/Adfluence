<template>
  <div>
    <div v-for="adRequest in filteredAdRequests" :key="adRequest.id" class="ad-request-card">
      <p>{{ influencerNames[adRequest.influencer_id] }} has accepted the ad {{  adNames[adRequest.ad_id]  }}. Make payment of {{ adRequest.payment }}.</p>
          <button @click="payNow(adRequest.id)" class="btn btn-primary"> PAY NOW</button>
        </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Pay',
  data() {
    return {
      adRequests: [],
      influencerNames: {},
      adNames: {},
      authToken: localStorage.getItem('authToken'),
      sponsorId: localStorage.getItem('sponsor_id')
    };
  },
  computed: {
    filteredAdRequests() {
      return this.adRequests.filter(adRequest => {
        return adRequest.sponsor_id === parseInt(this.sponsorId) && adRequest.status === 'accepted' && adRequest.ad_id != null;
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
        this.adRequests = response.data.data;
        this.adRequests.forEach(adRequest => {
          this.fetchInfluencerName(adRequest.influencer_id);
          this.fetchAdName(adRequest.ad_id);
        });
      })
      .catch(error => {
        console.error('Error fetching ad requests:', error);
      });
    },
    fetchInfluencerName(influencerId) {
      if (!this.influencerNames[influencerId]) {
        axios.get(`http://127.0.0.1:5000/api/influencer/${influencerId}`, {
          headers: {
            'Authorization': this.authToken
          }
        })
        .then(response => {
          this.influencerNames = { ...this.influencerNames, [influencerId]: response.data.data.influencer_name};
        })
        .catch(error => {
          console.error('Error fetching influencer name:', error);
        });
      }
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
    payNow(adRequestId, payment) {
      alert(`Payment of ${payment} made successfully`);
      axios.put(`http://127.0.0.1:5000/api/ad_request/${adRequestId}`, { status: 'paid' }, {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        alert("payment successfully sent")
        this.fetchAdRequests(); // Refresh the list
      })
      .catch(error => {
        console.error('Error updating ad request status:', error);
      });
    }
  },
  created() {
    this.fetchAdRequests();
  }
};
</script>

<style scoped>
.ad-request-card {
  width: 70vw;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.pay-now-button-container {
  display: flex;
  justify-content: flex-end;
}

.pay-now-button:hover {
  background-color: darkblue;
}
</style>