<!-- src/components/Profile.vue -->
<template>
  <div class="profile-card">
    <div class="profile-header">
      <img :src="profileImage" alt="Profile Image" class="profile-image" />
      <h2>{{ role }} Profile</h2>
    </div>
    <div class="profile-details">
      <p><strong>Username:</strong> {{ userDetails.username }}</p>
      <p><strong>Email:</strong> {{ userDetails.email }}</p>
      <p><strong>Role:</strong> {{ userDetails.role }}</p>
      <p v-if="role === 'influencer'"><strong>Category:</strong> {{ userDetails.category }}</p>
      <p v-if="role === 'influencer'"><strong>Niche:</strong> {{ userDetails.niche }}</p>
      <p v-if="role === 'influencer'"><strong>Reach:</strong> {{ userDetails.reach }}</p>
      <p v-if="role === 'sponsor'"><strong>Company:</strong> {{ userDetails.company }}</p>
      <p v-if="role === 'sponsor'"><strong>Industry:</strong> {{ userDetails.industry }}</p>
      <p v-if="role === 'sponsor'"><strong>Budget:</strong> {{ userDetails.budget }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      profileImage: 'https://i.pinimg.com/736x/b1/88/c6/b188c6801ad1d71d3c962c6e4aa2d0cf.jpg', // replace with actual path
      role: localStorage.getItem('role'),
      userDetails: {}
    };
  },
  mounted() {
    this.fetchUserDetails();
  },
  methods: {
    fetchUserDetails() {
      this.userDetails = {
        username: localStorage.getItem('username'),
        email: localStorage.getItem('email'),
        role: localStorage.getItem('role'),
        category: localStorage.getItem('category'),
        niche: localStorage.getItem('niche'),
        reach: localStorage.getItem('reach'),
        company: localStorage.getItem('Company_name'),
        industry: localStorage.getItem('Industry'),
        budget: localStorage.getItem('budget')
      };
    }
  }
};
</script>

<style scoped>
.profile-card {
  background-color: #9f7e69;
  color: #e3d5ca;
  border-radius: 18px;
  padding: 20px;
  margin: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.profile-header {
  display: flex;
  align-items: center;
}
.profile-image {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}
.profile-details {
  margin-top: 10px;
}
</style>