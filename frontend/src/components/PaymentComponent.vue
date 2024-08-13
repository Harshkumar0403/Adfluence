<template>
  <div class="payment-card">
    <form @submit.prevent="makePayment">
      <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">Make a Payment</h2>

      <div>
        <label for="influencer">Influencer Name  </label>
        <select id="influencer" v-model="selectedInfluencer" @change="fetchCampaigns">
          <option v-for="influencer in influencers" :key="influencer.influencer_id" :value="influencer.influencer_id">
            {{ influencer.influencer_name }}
          </option>
        </select>
      </div>

      <div>
        <label for="campaign">Campaign Name  </label>
        <select id="campaign" v-model="selectedCampaign" @change="fetchAds">
          <option v-for="campaign in campaigns" :key="campaign.id" :value="campaign.id">
            {{ campaign.name }}
          </option>
        </select>
      </div>

      <div>
        <label for="ad">Ad Name  </label>
        <select id="ad" v-model="selectedAd" @change="fetchBudget">
          <option v-for="ad in ads" :key="ad.id" :value="ad.id">
            {{ ad.name }}
          </option>
        </select>
      </div>

      <div>
        <label for="budget">Budget  </label>
        <input type="text" id="budget" v-model="budget" readonly />
      </div>

      <div>
        <label for="cardHolderName">Card Holder Name  </label>
        <input type="text" id="cardHolderName" v-model="cardHolderName" required />
      </div>

      <div>
        <label for="cardNumber">Card Number  </label>
        <input type="text" id="cardNumber" v-model="cardNumber" required />
      </div>

      <div class="cvv-container">
        <label for="cvv">CVV  </label>
        <input type="text" id="cvv" v-model="cvv" required />
      </div>

      <div>
        <input type="checkbox" id="terms" v-model="termsAccepted" required />
        <label for="terms">I agree to the terms and conditions</label>
      </div>

      <div class="pay-now-button-container">
        <button type="submit" class="pay-now-button"> PAY NOW</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PaymentComponent',
  data() {
    return {
      selectedInfluencer: '',
      selectedCampaign: '',
      selectedAd: '',
      budget: '',
      cardHolderName: '',
      cardNumber: '',
      cvv: '',
      termsAccepted: false,
      influencers: [],
      campaigns: [],
      ads: [],
      authToken: localStorage.getItem('authToken')
    };
  },
  methods: {
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
    fetchCampaigns() {
      axios.get('http://127.0.0.1:5000/api/campaign', {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.campaigns = response.data.data;
      })
      .catch(error => {
        console.error('Error fetching campaigns:', error);
      });
    },
    fetchAds() {
      axios.get(`http://127.0.0.1:5000/api/Ad?campaign_id=${this.selectedCampaign}`, {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.ads = response.data.data;
      })
      .catch(error => {
        console.error('Error fetching ads:', error);
      });
    },
    fetchBudget() {
      axios.get(`http://127.0.0.1:5000/api/Ad/${this.selectedAd}`, {
        headers: {
          'Authorization': this.authToken
        }
      })
      .then(response => {
        this.budget = response.data.data.budget;
      })
      .catch(error => {
        console.error('Error fetching budget:', error);
      });
    },
    makePayment() {
      alert(`Payment of ${this.budget} made successfully.`);
      // Here you can add additional logic for processing the payment.
      location.reload();
    }
  },
  created() {
    this.fetchInfluencers();
    this.fetchCampaigns();
  }
};
</script>

<style scoped>
.payment-card {
  width: 70vw;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  position: relative;
  background-color: #faedcd;
}
select{
    margin-left:10px;
}
input{
    margin-left:10px;
}
/* .pay-now-button-container {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
} */

.pay-now-button {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.pay-now-button:hover {
  background-color: darkblue;
}
</style>
