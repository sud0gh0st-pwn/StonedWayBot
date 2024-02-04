<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/menu">Menu</router-link> |
    <router-link to="/checkout">Basket</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #9DBC98;
  background-color: #637E76;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #9DBC98;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #c9e0c6;
  text-decoration: none;
}
</style>
