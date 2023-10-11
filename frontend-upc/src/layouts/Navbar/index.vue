<script setup>
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline";

const navigation = [
  {
    name: "Dashboard",
    current: false,
    menu: {
      1: { link: "/dashStu", name: "Estudiantes" },
      2: { link: "/dashGra", name: "Egresados" },
    },
  },
  {
    name: "Estudiantes",
    current: false,
    menu: {
      1: { link: "/inscripcion", name: "Inscripción" },
      2: { link: "/consulta", name: "Consulta" },
    },
  },
  {
    name: "Egresados",
    current: false,
    menu: {
      1: { link: "/inscripcion", name: "Inscripción" },
      2: { link: "/consulta_egresados", name: "Consulta" },
    },
  },
];
</script>

<template>
  <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
          >
            <span class="absolute -inset-0.5" />
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-between"
        >
          <div class="flex flex-shrink-0 items-center">
            <img src="@/assets/logo.png" width="80" height="80" class="px-4" />
            <router-link to="/" class="text-2xl text-white"
              >Proyecto institucional
            </router-link>
          </div>
          <div class="hidden sm:ml-6 sm:block mt-1">
            <div class="flex space-x-8">
              <div
                v-for="item in navigation"
                :key="item.name"
                :href="item.href"
                :class="[
                  item.current
                    ? 'bg-gray-900 text-white hover:bg-gray-600'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white text',
                  'rounded-md px-3 py-2 text-lg font-medium',
                ]"
                :aria-current="item.current ? 'page' : undefined"
              >
                <Menu as="div" class="relative ml-3 text-center">
                  <div>
                    <MenuButton>
                      {{ item.name }}
                      <span class="absolute -inset-1.5" />
                      <span class="sr-only"></span>
                    </MenuButton>
                  </div>
                  <transition
                    enter-active-class="transition ease-out duration-100"
                    enter-from-class="transform opacity-0 scale-95"
                    enter-to-class="transform opacity-100 scale-100"
                    leave-active-class="transition ease-in duration-75"
                    leave-from-class="transform opacity-100 scale-100"
                    leave-to-class="transform opacity-0 scale-95"
                  >
                    <MenuItems
                      class="absolute z-10 mt-3 w-40 rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                      v-if="item.menu"
                    >
                      <MenuItem
                        v-for="data in item.menu"
                        :key="data"
                        v-slot="{ active }"
                      >
                        <router-link
                          :to="data.link"
                          :class="[
                            active ? 'bg-gray-100' : '',
                            'block px-4 py-2 text-base text-gray-800',
                          ]"
                        >
                          {{ data.name }}
                        </router-link>
                      </MenuItem>
                    </MenuItems>
                  </transition>
                </Menu>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 px-2 pb-3 pt-2">
        <DisclosureButton
          v-for="item in navigation"
          :key="item.name"
          as="a"
          :href="item.href"
          :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-gray-300 hover:bg-gray-700 hover:text-white',
            'block rounded-md px-3 py-2 text-base font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
          >{{ item.name }}</DisclosureButton
        >
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
